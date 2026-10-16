# Document Formatting Defaults

Formatting defaults for all generated documents. The destination is **Notion**, which imports clean Markdown well. Don't generate HTML, font/size hints, or page-margin styling. Notion controls all of that.

## Output Format

- Write plain Markdown. Notion handles styling on import.
- No HTML wrappers, no inline CSS, no `<style>` blocks, no `@page` rules.
- No font, size, color, or margin directives. Notion uses its own theme.

## Headings

- Notion supports H1, H2, H3 only. H4+ in Markdown is converted to bold text on import, which breaks navigation and the table of contents. Don't use `####` or deeper.
- The first `# Heading` in the file becomes the page title in Notion. There should be exactly one H1 per file, at the top.
- Body sections should start at `##`. Subsections use `###`. If you need a fourth level, restructure the content instead.
- Use bold (`**Label**`) for emphasis within a section, not as a stand-in for a heading.

## Tables

- Use standard Markdown table syntax. Notion imports these as "simple tables."
- Keep column counts reasonable (typically ≤5). Very wide tables are hard to read in Notion's page layout.
- Don't add blank lines inside table blocks. One blank line before and after the table is enough.
- Don't try to color cells or rows. Notion's simple tables don't support cell styling on import.

## Dashes

- **Never use em dashes (U+2014).** This is a hard rule for all documents and chat replies.
- Never use en dashes or hyphens as sentence connectors or parenthetical separators either.
- Rewrite the sentence instead: use periods, semicolons, colons, commas, or parentheses.
- Only use hyphens where a normal person would (e.g., compound words like "top-of-funnel", phone numbers, numeric ranges like "84-86%").

## Dividers

- `---` on its own line works in Notion as a divider block. Use sparingly; heading hierarchy usually does the job better.

## Callouts and quotes

- Markdown blockquotes (`> ...`) import as Notion quote blocks. Use them for emphasis or pulled quotes.
- Notion's callout block (the colored box with an icon) doesn't have a standard Markdown equivalent. If a callout is desired, write a blockquote and the user can convert it to a callout in Notion.

## Code

- Use fenced code blocks with language tags (```` ```python ````). Notion preserves the language and syntax highlighting.

## Lists

- Standard Markdown bullets (`-`) and numbered lists work as expected.
- Indent nested items with two spaces.
- Don't mix `-` and `*` bullet markers in the same file.

## Links

- Use inline Markdown links: `[label](url)`. Notion converts these to clickable links.
- Avoid bare URLs in body text; wrap them in a link with a meaningful label.

## Notion page updates

When editing an existing Notion page (not creating a new one):

- **Preserve comments.** Never resolve or delete discussions unless the user explicitly asks. Inline comments are anchored to specific text; replacing whole-page content detaches or loses them.
- **Before editing:** `notion-fetch` with `include_discussions: true`, then `notion-get-comments` if needed. Note which passages have open threads.
- **Prefer surgical edits:** use `update_content` (search-and-replace) over `replace_content` whenever the change is localized. Match `old_str` closely to text that carries comments so threads stay on the right passage.
- **When a full rewrite is required:** keep commented phrases verbatim where possible, or re-apply the same wording in the equivalent bullet/row so the comment remains relevant. After updating, re-fetch with `include_discussions: true` and flag any threads that may have drifted.
