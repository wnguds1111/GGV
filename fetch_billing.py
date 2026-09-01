import urllib.request
import urllib.parse
import json
import re
import http.cookiejar

# Cookie jar to maintain session
jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-TW,zh;q=0.9',
}

# Step 1: Load billing page to get CSRF token + cookies
print("Step 1: Loading Billing page...")
req = urllib.request.Request('https://www.gnjoy.hk/Billing', headers=headers)
try:
    with opener.open(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        token_match = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', html)
        if token_match:
            csrf_token = token_match.group(1)
            print(f"CSRF Token found: {csrf_token[:30]}...")
        else:
            print("CSRF Token not found in page")
            csrf_token = ''
except Exception as e:
    print(f"Error loading page: {e}")
    csrf_token = ''

# Step 2: For each game, call the payment list API
games = [
    ('ROBA', 'RO仙境傳說：初心之戰'),
    ('ROO',  'RO仙境傳說：愛如初見'),
    ('RORB', 'RO仙境傳說：重生'),
    ('ROTL', 'RO仙境傳說：曙光'),
]

results = {}

for game_id, game_name in games:
    print(f"\n=== Fetching payment list for {game_id} ({game_name}) ===")
    
    post_data = urllib.parse.urlencode({
        'gameid': game_id,
        'servernamepre': '',
        '__RequestVerificationToken': csrf_token
    }).encode('utf-8')
    
    api_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.gnjoy.hk/Billing',
        'Origin': 'https://www.gnjoy.hk',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }
    
    req = urllib.request.Request(
        'https://www.gnjoy.hk/Billing/GetServerListAndPaymentListNew',
        data=post_data,
        headers=api_headers,
        method='POST'
    )
    
    try:
        with opener.open(req, timeout=15) as resp:
            raw = resp.read().decode('utf-8', errors='ignore')
            print(f"Response length: {len(raw)}")
            print(f"Raw (first 2000): {raw[:2000]}")
            results[game_id] = raw
    except Exception as e:
        print(f"Error: {e}")
        results[game_id] = None

# Save results
with open('billing_api_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
    
print("\nDone! Results saved to billing_api_results.json")
