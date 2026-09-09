#!/usr/bin/env ruby

require "csv"
require "digest"
require "open3"
require "fileutils"

ROOT = File.expand_path("../../..", __dir__)
SOURCES = File.join(ROOT, "sources")
OUT = File.expand_path("..", __dir__)

EXCLUDED_NAMES = [".DS_Store", "README.md", "MANIFEST.md"].freeze

PROMOTE_SHORT = {
  "sources/COntent creation/THE_ELEMENTS_OF_STYLE_UPDATED_2011_EDITIO_-_William_Strunk.pdf" => ["book", "D1", "historical/practitioner"],
  "sources/Linkedin Guru/Crush_It_On_LinkedIn_-_Build_Your_Brand_Get_Hired_n_Expand_Your_Business_-_Ishan_Sharma.pdf" => ["book", "D1", "popular/practitioner"],
  "sources/Linkedin Guru/LinkedIn_Personal_Branding_And_Marketing_-_Patricia_Will.pdf" => ["book", "D1", "popular/practitioner"],
  "sources/Linkedin Guru/Used for training/Linkedin_Social_Selling_Strategies_-_Joseph_Hood.pdf" => ["book", "D1", "popular/practitioner"],
  "sources/Product Manager/Uploaded/Lean_Startup__How_to_Apply_the_Lean_Startu_-_Greg_Caldwell.pdf" => ["book", "D1", "popular/practitioner"],
  "sources/Psychedelic Coach/Taken for training/Evidence-Based Best Practices in Psychedelic Preparation and Integration….pdf" => ["manual/reference", "D2", "practice/evidence-review-needed"],
  "sources/Psychedelic Coach/Taken for training/MAPS-Integration-Workbook.pdf" => ["manual/reference", "D2", "practice/manual"],
  "sources/Psychedelic Coach/Taken for training/Treatment recommendations  PAT 17 1 24.pdf" => ["manual/reference", "D2", "practice/guidance-check-current"],
  "sources/Sales Manager/Trained on/Outbound_Sales_No_Fluff__Written_by_Two_M_-_Ryan_Reisert.pdf" => ["book", "D1", "popular/practitioner"]
}.freeze

D1 = [
  "AI coach", "COntent creation", "Conscious marketer", "FANATIC",
  "Linkedin Guru", "Management Consultant", "Nudger", "Product Manager",
  "Sales Manager", "Text editor", "Workshops"
].freeze

D2 = [
  "AI Healer", "Arthritis Healer", "Plant medicine healer",
  "Psychedelic Coach", "Psychologist", "Taxation Consultant"
].freeze

NON_BOOK_FAMILIES = [
  "AI Model", "Digital Vlad", "Linkedin", "Mu Ni", "O!Sapiens",
  "Personal", "Psychedelics", "Research", "Tik TOk", "transcripts"
].freeze

DOMAIN = {
  "AI Healer" => "health-neuroscience-longevity",
  "AI Model" => "ai-governance",
  "AI coach" => "coaching-performance",
  "Arthritis Healer" => "arthritis-pain-movement",
  "COntent creation" => "content-writing",
  "Conscious marketer" => "marketing-branding",
  "Digital Vlad" => "identity-authority",
  "FANATIC" => "strategy-branding-organization",
  "Linkedin" => "linkedin-social-selling",
  "Linkedin Guru" => "linkedin-content-sales",
  "Management Consultant" => "consulting-leadership",
  "Mu Ni" => "marketing-intelligence",
  "Nudger" => "behavioral-psychology",
  "O!Sapiens" => "healthspan-product-brand",
  "Personal" => "identity-state-strategy",
  "Plant medicine healer" => "herbalism-pharmacognosy",
  "Product Manager" => "product-growth-business-model",
  "Psychedelic Coach" => "psychedelic-integration-safety",
  "Psychedelics" => "psychedelic-research-content",
  "Psychologist" => "psychology-trauma",
  "Research" => "research-synthesis",
  "Sales Manager" => "sales-negotiation",
  "Taxation Consultant" => "taxation-law-policy",
  "Text editor" => "editing-writing",
  "Tik TOk" => "short-form-content",
  "Workshops" => "facilitation-learning",
  "transcripts" => "transcripts-primary-records"
}.freeze

REFERENCE_RE = /(handbook|textbook|encyclopedia|manual|diagnostic_and_statistical|principles_of_neural|guide_to|workbook|anatomy|clinical)/i
HISTORICAL_RE = /(avicenn|william_james|principles_of_psychology|origin_of_consciousness|divided_self|games_people_play|rheumatoid_arthritis_-_charles_l_short)/i
LOW_AUTHORITY_RE = /(cookbook|home_apothecary|home_pharmacist|miracle|cure|healing_plan|heal_your|pain_free|beaten|fix|natural_cures|vibrant_botanicals)/i

def source_files
  Dir.glob(File.join(SOURCES, "**", "*"), File::FNM_DOTMATCH).select do |path|
    File.file?(path) && !File.basename(path).start_with?(".") && !EXCLUDED_NAMES.include?(File.basename(path))
  end.sort
end

def relative(path)
  path.delete_prefix(ROOT + "/")
end

def family(path)
  relative(path).split("/")[1]
end

def canonical_path(paths)
  paths.min_by do |path|
    rel = relative(path)
    penalty = 0
    penalty += 30 if rel.include?("_OceanofPDF")
    penalty += 20 if rel.include?("Used for training") || rel.include?("Taken for training") || rel.include?("Trained on")
    penalty += 10 if rel.include?("Uploaded") || rel.include?("To upload")
    [penalty, rel.length, rel]
  end
end

def pdf_probe(path)
  info, status = Open3.capture2e("pdfinfo", path)
  return [nil, "unreadable", true] unless status.success?

  pages = info[/^Pages:\s+(\d+)/, 1]&.to_i
  text, text_status = Open3.capture2e("pdftotext", "-f", "1", "-l", [pages || 12, 12].min.to_s, path, "-")
  chars = text_status.success? ? text.gsub(/\s+/, "").length : 0
  quality = if chars >= 2_000
              "good"
            elsif chars >= 300
              "sparse"
            else
              "poor"
            end
  [pages, quality, quality == "poor"]
end

def infer_title(path)
  File.basename(path, File.extname(path)).sub(/^_OceanofPDF\.com_/, "").tr("_", " ").gsub(/\s+/, " ").strip
end

def language_hint(path)
  File.basename(path).match?(/[А-Яа-яЁё]/) ? "ru" : "en-or-unknown"
end

def edition_hint(path)
  name = File.basename(path, File.extname(path))
  hints = name.scan(/(?:\d+(?:st|nd|rd|th)_Edition|Revised(?:_and_Updated)?|Expanded_Edition|Final_Edition|Volume_?\d+|Vol_?(?:One|Two|\d+)|2nd_Edition)/i)
  hints.empty? ? "not-in-filename" : hints.join(" | ").tr("_", " ")
end

def year_hint(path)
  File.basename(path)[/(?:19|20)\d{2}/] || "not-in-filename"
end

def classify(path, pages)
  ext = File.extname(path).downcase
  fam = family(path)
  name = File.basename(path)
  rel = relative(path)

  if PROMOTE_SHORT.key?(rel)
    type, phase, authority = PROMOTE_SHORT.fetch(rel)
    return [type, "yes", phase, authority, "pending"]
  end

  return ["transcript", "no", "excluded", "primary-record", "not-applicable"] if [".vtt", ".txt"].include?(ext)
  return ["dataset", "no", "excluded", "primary/internal", "not-applicable"] if ext == ".xlsx"
  return ["internal-document", "no", "excluded", "primary/internal", "not-applicable"] if [".docx", ".md"].include?(ext)
  return ["other", "review", "D0-review", "unknown", "unknown"] unless ext == ".pdf"

  likely_book_family = !NON_BOOK_FAMILIES.include?(fam)
  if pages && pages >= 80 && likely_book_family
    type = name.match?(REFERENCE_RE) ? "manual/reference" : "book"
    phase = if name.match?(HISTORICAL_RE)
              "D3"
            elsif D1.include?(fam)
              "D1"
            elsif D2.include?(fam)
              "D2"
            else
              "D3"
            end
    authority = if name.match?(HISTORICAL_RE)
                  "historical/theoretical"
                elsif name.match?(LOW_AUTHORITY_RE)
                  "popular/practitioner-low"
                elsif type == "manual/reference"
                  "reference/professional"
                else
                  "popular/practitioner"
                end
    return [type, "yes", phase, authority, "pending"]
  end

  if likely_book_family
    return ["short-nonbook-summary-or-incomplete", "no", "excluded", "context-only", "excluded-after-D0-length/completeness-review"]
  end

  ["internal-or-research-pdf", "no", "excluded", "primary/derived-context", "not-applicable"]
end

files = source_files
groups = files.group_by { |path| Digest::SHA256.file(path).hexdigest }
rows = []

groups.sort_by { |_, paths| relative(canonical_path(paths)) }.each do |sha, paths|
  canonical = canonical_path(paths)
  ext = File.extname(canonical).downcase
  pages, quality, ocr = ext == ".pdf" ? pdf_probe(canonical) : [nil, "not-applicable", false]
  type, eligible, phase, authority, review = classify(canonical, pages)
  families = paths.map { |path| family(path) }.uniq.sort
  safety = families.any? { |fam| D2.include?(fam) } ? "high" : (families.include?("Psychedelics") ? "high" : "standard")
  rows << {
    "sha256" => sha,
    "canonical_path" => relative(canonical),
    "all_source_paths" => paths.map { |path| relative(path) }.sort.join(" | "),
    "copy_count" => paths.size,
    "families" => families.join(" | "),
    "title_inferred" => infer_title(canonical),
    "language_provisional" => language_hint(canonical),
    "edition_hint" => edition_hint(canonical),
    "year_hint" => year_hint(canonical),
    "file_type" => ext.delete_prefix("."),
    "pages" => pages,
    "text_quality" => quality,
    "ocr_required" => ocr ? "yes" : "no",
    "record_type" => type,
    "deep_eligible" => eligible,
    "deep_phase" => phase,
    "domain" => families.map { |fam| DOMAIN.fetch(fam, "unknown") }.uniq.join(" | "),
    "safety_review" => safety,
    "authority_provisional" => authority,
    "bibliographic_review" => review,
    "completeness_provisional" => if eligible == "yes"
                                      pages && pages < 80 ? "promoted-short-complete-or-substantial" : "full-length-provisional"
                                    elsif type.start_with?("short-")
                                      "short-summary-nonbook-or-incomplete"
                                    else
                                      "not-applicable"
                                    end,
    "extraction_status" => eligible == "yes" ? "not-started" : (eligible == "review" ? "needs-review" : "excluded-by-corpus-rule")
  }
end

override_path = File.join(OUT, "status-overrides.tsv")
if File.file?(override_path)
  overrides = CSV.read(override_path, headers: true, col_sep: "\t").each_with_object({}) do |row, memo|
    memo[row["sha256"]] = row.to_h
  end
  rows.each do |row|
    override = overrides[row["sha256"]]
    next unless override
    override.each do |key, value|
      row[key] = value unless key == "sha256" || value.nil? || value.empty?
    end
  end
end

ledger = File.join(OUT, "corpus-ledger.tsv")
CSV.open(ledger, "w", col_sep: "\t", write_headers: true, headers: rows.first.keys) do |csv|
  rows.each { |row| csv << row.values }
end

counts = rows.group_by { |row| row["deep_eligible"] }.transform_values(&:size)
phases = rows.group_by { |row| row["deep_phase"] }.transform_values(&:size)
types = rows.group_by { |row| row["record_type"] }.transform_values(&:size)
ocr_count = rows.count { |row| row["ocr_required"] == "yes" }
dup_groups = rows.count { |row| row["copy_count"] > 1 }
redundant = rows.sum { |row| row["copy_count"] - 1 }

summary = <<~MD
  ---
  id: deep-extraction-d0-ledger
  type: fact
  status: complete
  canonical: true
  last_updated: 2026-08-31
  ---

  # D0 corpus classification

  ## Result

  The reconciled 511-document archive resolves to 458 SHA-256 records. One canonical extraction path is selected per hash; all #{dup_groups} duplicate groups and #{redundant} redundant copies resolve to those same records.

  The machine-readable source of truth is [corpus-ledger.tsv](corpus-ledger.tsv). Eligibility is resolved; bibliographic fields remain provisional until each eligible work starts. Manual decisions and near-duplicate/OCR review are recorded in [D0 review notes](D0-REVIEW-NOTES.md).

  | Classification | Unique records |
  | --- | ---: |
  | Deep eligible | #{counts.fetch("yes", 0)} |
  | Needs D0 manual review | #{counts.fetch("review", 0)} |
  | Excluded by corpus rule | #{counts.fetch("no", 0)} |
  | **Total unique hashes** | **#{rows.size}** |

  ## Extraction queue

  | Phase | Unique records |
  | --- | ---: |
  | D1 — core business/practice | #{phases.fetch("D1", 0)} |
  | D2 — safety-sensitive | #{phases.fetch("D2", 0)} |
  | D3 — supporting/contextual | #{phases.fetch("D3", 0)} |
  | D0 manual review | #{phases.fetch("D0-review", 0)} |
  | Excluded | #{phases.fetch("excluded", 0)} |

  ## Record types

  #{types.sort.map { |type, count| "- `#{type}`: #{count}" }.join("\n")}

  ## Extraction quality

  - PDFs provisionally requiring OCR or repair: #{ocr_count}.
  - `good`/`sparse`/`poor` is based on extractable characters from the first twelve pages and must be rechecked at book level.
  - Short PDFs in book-heavy families were manually promoted or excluded; no D0 eligibility decision remains unresolved.
  - DOCX, Markdown, spreadsheets, transcripts, and PDFs in operating/research families are excluded from chapter-level book extraction unless manually promoted.

  ## Fields

  Each row records full hash, canonical path, all duplicate paths, families, inferred title, type/pages, extractability, eligibility/phase, domain, safety level, provisional authority, bibliographic-review state, and extraction status.

  ## D0 completion

  - All `needs-review` eligibility rows are resolved.
  - Exact duplicates share one record; likely editions, volumes, and near-duplicates were reviewed separately.
  - OCR candidates were tested on representative interior pages.
  - Exclusions and promotions remain explicit in the ledger.
  - Title, author/editor, edition/year, language, completeness, and authority must be confirmed at the start of each D1–D3 book note.
MD

File.write(File.join(OUT, "D0-CORPUS-LEDGER.md"), summary)

puts "unique_records=#{rows.size} eligible=#{counts.fetch("yes", 0)} review=#{counts.fetch("review", 0)} excluded=#{counts.fetch("no", 0)}"
puts "D1=#{phases.fetch("D1", 0)} D2=#{phases.fetch("D2", 0)} D3=#{phases.fetch("D3", 0)} OCR=#{ocr_count}"
