import requests, re

def fetch_js(url):
    r = requests.get(url)
    if r.status_code != 200:
        print(f"❌ Failed: {r.status_code}"); return None
    print(f"✅ JS Fetched | Size: {len(r.content)} bytes | Type: {r.headers.get('Content-Type', 'Unknown')}")
    return r.text

def extract(js, pattern):
    return re.findall(pattern, js)

url = "https://github.githubassets.com/assets/ui_packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfill_ts-ui_packages_re-8d43b0-a64c4553bcdf.js"  
js = fetch_js(url)

if js:
    funcs = extract(js, r'function\s+(\w+)\s*\((.*?)\)')
    vars_ = set(sum(extract(js, r'var\s+(\w+)\s*=|let\s+(\w+)\s*=|const\s+(\w+)\s*='), ())) - {''}
    logs = extract(js, r'console\.log\((.*?)\)')

    if funcs: print("\n🔍 Functions:", *[f"➤ {f}({p})" for f, p in funcs], sep="\n")
    if vars_: print("\n📌 Variables:", *[f"➤ {v}" for v in vars_], sep="\n")
    if logs: print("\n🖥️ Logs:", *[f"➤ console.log({l})" for l in logs], sep="\n")

    print("\n🎯 Analysis Done.")
