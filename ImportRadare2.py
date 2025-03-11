import requests, re

def fetch_js(url):
    print("\n🌐 Fetching JavaScript...")
    r = requests.get(url)
    if r.status_code != 200:
        print(f"❌ Fetch Failed: {r.status_code}"); return None
    print(f"✅ Fetched | Size: {len(r.content)} bytes | Type: {r.headers.get('Content-Type', 'Unknown')}\n")
    return r.text

def extract(js, pattern):
    return re.findall(pattern, js)

def display_chart(title, items, prefix="➤"):
    if items:
        print(f"\n📌 {title}")
        for item in items:
            print(f"   {prefix} {item}")

url = "https://github.githubassets.com/assets/ui_packages_promise-with-resolvers-polyfill_promise-with-resolvers-polyfill_ts-ui_packages_re-8d43b0-a64c4553bcdf.js"  
js = fetch_js(url)

if js:
    funcs = extract(js, r'function\s+(\w+)\s*\((.*?)\)')
    vars_ = set(sum(extract(js, r'var\s+(\w+)\s*=|let\s+(\w+)\s*=|const\s+(\w+)\s*='), ())) - {''}
    logs = extract(js, r'console\.log\((.*?)\)')

    print("\n🔽 JS Analysis Flowchart 🔽\n")

    print("🛠️  JavaScript Execution")
    print("   ├── 📂 Variables")
    for v in vars_: print(f"   │   ├── 🏷️ {v}")
    
    print("   ├── 🔧 Functions")
    for f, p in funcs: print(f"   │   ├── 🔹 {f}({p})")
    
    print("   ├── 🖥️ Console Logs")
    for l in logs: print(f"   │   ├── 📝 console.log({l})")

    print("\n🎯 Analysis Complete.")
