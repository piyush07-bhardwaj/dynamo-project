There is an Apache-style access log at /app/access.log.

Analyze the log and produce a JSON report at:

/app/report.json

Success criteria:

1. Create the file /app/report.json.
2. The file must contain valid JSON.
3. The JSON must contain a field named "total_requests" whose value is 6.
4. The JSON must contain a field named "unique_ips" whose value is 3.
5. The JSON must contain a field named "top_path" whose value is "/index.html".