# hopper-radare2

Fetch JavaScript from a URL

Uses requests.get(url) to retrieve JavaScript content.
Displays metadata (file size, content type, and URL).
Extract JavaScript Functions

Uses regex to find function definitions (function functionName(params) { ... }).
Lists all function names and their parameters.
Extract Variables & Console Logs

Identifies var, let, and const declarations.
Finds console.log(...) statements.
Display Results in an Organized Manner

Functions are listed with their names and parameters.
Variables and console logs are shown separately.
Helps users understand the script structure at a glance.
