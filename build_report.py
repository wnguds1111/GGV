
# Build the complete HTML report
lines = [
    '<!DOCTYPE html>',
    '<html lang="ko">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>GNJOY HK - 게임별 결제 채널 완전 분석 보고서</title>',
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">',
    '<style>',
    ':root{--p:#C8102E;--bg:#0D0F14;--bgc:#161922;--bgp:#1E2230;--bd:#2A2F45;--tx:#E8EAF0;--tm:#7B82A0;}',
    '*{margin:0;padding:0;box-sizing:border-box;}',
    'body{font-family:"Noto Sans KR",sans-serif;background:var(--bg);color:var(--tx);line-height:1.6;}',
    '.hd{background:linear-gradient(135deg,#C8102E,#6B0418 50%,#1a1a2e);padding:36px 48px 28px;border-bottom:1px solid rgba(200,16,46,.4);}',
    '.hd h1{font-size:26px;font-weight:900;color:#fff;margin-bottom:10px;}',
    '.hd-sub{display:flex;gap:12px;flex-wrap:wrap;}',
    '.hd-chip{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:6px;padding:4px 14px;font-size:11px;color:rgba(255,255,255,.85);}',
    '.hd-chip b{color:#fff;}',
    '.nav{background:var(--bgc);border-bottom:1px solid var(--bd);padding:0 48px;display:flex;overflow-x:auto;position:sticky;top:0;z-index:100;box-shadow:0 4px 20px rgba(0,0,0,.4);}',
    '.nb{padding:15px 22px;background:none;border:none;border-bottom:3px solid transparent;color:var(--tm);font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;transition:.2s;font-family:inherit;}',
    '.nb:hover{color:var(--tx);}',
    '.nb.active{color:#FF8CA0;border-bottom-color:var(--p);}',
    '.wrap{max-width:1600px;margin:0 auto;padding:36px 48px;}',
    '.sec{display:none;}.sec.active{display:block;}',
    '.gh{display:flex;align-items:center;gap:18px;margin-bottom:28px;padding:22px 26px;background:var(--bgc);border-radius:14px;border:1px solid var(--bd);position:relative;overflow:hidden;}',
    '.gh::before{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--gc,var(--p));}',
    '.gb{background:var(--gc,var(--p));color:#fff;font-size:13px;font-weight:800;padding:5px 13px;border-radius:7px;flex-shrink:0;}',
    '.gt h2{font-size:20px;font-weight:800;margin-bottom:3px;}',
    '.gt p{font-size:12px;color:var(--tm);}',
    '.gm{display:flex;gap:8px;flex-wrap:wrap;}',
    '.mt{background:rgba(255,255,255,.06);border:1px solid var(--bd);border-radius:5px;padding:3px 10px;font-size:11px;color:var(--tm);}',
    '.mt b{color:var(--tx);}',
    '.ntc{border-radius:10px;padding:14px 18px;margin-bottom:22px;font-size:12.5px;}',
    '.ntc h4{font-size:12px;font-weight:700;margin-bottom:7px;}',
    '.ntc ul{padding-left:15px;}.ntc li{margin-bottom:3px;}',
    '.pts{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:22px;}',
    '.pt{padding:7px 16px;background:var(--bgp);border:1px solid var(--bd);border-radius:7px;color:var(--tm);font-size:12px;font-weight:600;cursor:pointer;transition:.2s;font-family:inherit;}',
    '.pt:hover{border-color:var(--p);color:var(--tx);}',
    '.pt.active{background:var(--p);border-color:var(--p);color:#fff;}',
    '.pt.dis{opacity:.35;cursor:not-allowed;}',
    '.pp{display:none;}.pp.active{display:block;}',
    '.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:18px;margin-bottom:22px;}',
    '.cc{background:var(--bgp);border:1px solid var(--bd);border-radius:13px;overflow:hidden;transition:.2s;}',
    '.cc:hover{border-color:var(--cc,var(--p));box-shadow:0 4px 18px rgba(0,0,0,.3);transform:translateY(-2px);}',
    '.ch{background:var(--cc,var(--p));padding:13px 16px;display:flex;align-items:center;gap:9px;}',
    '.ci{width:34px;height:34px;background:rgba(255,255,255,.2);border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}',
    '.cn{font-size:14px;font-weight:700;color:#fff;}',
    '.cs{font-size:11px;color:rgba(255,255,255,.75);margin-top:1px;}',
    '.cb{padding:14px 16px;}',
    '.al{font-size:10px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}',
    '.ag{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:10px;}',
    '.ac{background:rgba(255,255,255,.06);border:1px solid var(--bd);border-radius:5px;padding:3px 9px;font-size:13px;font-weight:600;color:var(--tx);}',
    '.nw{background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.25);border-radius:7px;padding:9px 12px;font-size:11.5px;color:#FCD34D;margin-top:8px;}',
    '.ni{background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.25);border-radius:7px;padding:9px 12px;font-size:11.5px;color:#93C5FD;margin-top:8px;}',
    '.st{font-size:17px;font-weight:800;margin-bottom:18px;display:flex;align-items:center;gap:10px;}',
    '.st::after{content:"";flex:1;height:1px;background:var(--bd);}',
    '.tw{overflow-x:auto;border-radius:13px;border:1px solid var(--bd);margin-bottom:30px;}',
    'table{width:100%;border-collapse:collapse;font-size:13px;}',
    'th{background:var(--bgp);padding:13px 14px;text-align:left;font-weight:700;color:var(--tm);border-bottom:1px solid var(--bd);white-space:nowrap;}',
    'td{padding:11px 14px;border-bottom:1px solid rgba(42,47,69,.6);vertical-align:top;}',
    'tr:last-child td{border-bottom:none;}',
    'tr:hover td{background:rgba(255,255,255,.02);}',
    '.tdy{color:#10B981;font-weight:700;}',
    '.tdn{color:var(--tm);}',
    '.ov{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:36px;}',
    '.oc{background:var(--bgc);border:1px solid var(--bd);border-radius:13px;padding:18px;position:relative;overflow:hidden;transition:.2s;}',
    '.oc:hover{border-color:var(--gc,var(--p));transform:translateY(-2px);}',
    '.oc::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:var(--gc,var(--p));}',
    '.oc-code{font-size:10px;font-weight:700;letter-spacing:2px;color:var(--tm);text-transform:uppercase;margin-bottom:5px;}',
    '.oc-nm{font-size:14px;font-weight:800;margin-bottom:10px;}',
    '.oc-s{display:flex;flex-direction:column;gap:3px;}',
    '.oc-r{display:flex;justify-content:space-between;font-size:11px;}',
    '.oc-rl{color:var(--tm);}',
    '.oc-rv{font-weight:700;}',
    '@media(max-width:1100px){.wrap{padding:22px 18px;}.ov{grid-template-columns:repeat(2,1fr);}.cg{grid-template-columns:1fr;}.hd{padding:22px 18px;}.nav{padding:0 18px;}}',
    '</style>',
    '</head>',
    '<body>',
]

# HEADER
lines += [
    '<div class="hd">',
    '<h1>🎮 GNJOY HK 게임별 결제 채널 완전 분석 보고서</h1>',
    '<div class="hd-sub">',
    '<span class="hd-chip">분석 게임 <b>4종</b></span>',
    '<span class="hd-chip">결제 카테고리 <b>8개</b></span>',
    '<span class="hd-chip">수집방법 <b>실계정 브라우저 직접클릭</b></span>',
    '<span class="hd-chip">ROO 금액 <b>실계정 직접 확인 완료</b></span>',
    '<span class="hd-chip">날짜 <b>2026-08-03</b></span>',
    '</div></div>',
]

# NAV
lines += [
    '<div class="nav">',
    '<button class="nb active" onclick="sG(event,\'ov\')">📊 전체 비교</button>',
    '<button class="nb" onclick="sG(event,\'roba\')">🔴 ROBA 初心之戰</button>',
    '<button class="nb" onclick="sG(event,\'roo\')">🔵 ROO 愛如初見</button>',
    '<button class="nb" onclick="sG(event,\'rorb\')">🟢 RORB 重生</button>',
    '<button class="nb" onclick="sG(event,\'rotl\')">🟡 ROTL 曙光</button>',
    '</div>',
    '<div class="wrap">',
]

# === OVERVIEW SECTION ===
lines += [
    '<div id="ov" class="sec active">',
    '<div class="st">🎯 게임별 결제 인프라 요약</div>',
    '<div class="ov">',
    # ROBA
    '<div class="oc" style="--gc:#C8102E"><div class="oc-code">ROBA</div><div class="oc-nm">初心之戰</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">彩鑽</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">4종</span></div>',
    '<div class="oc-r"><span class="oc-rl">港澳 지원</span><span class="oc-rv">✅</span></div>',
    '</div></div>',
    # ROO
    '<div class="oc" style="--gc:#3B82F6"><div class="oc-code">ROO</div><div class="oc-nm">愛如初見</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">喵喵果實</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">16종 ★최다</span></div>',
    '<div class="oc-r"><span class="oc-rl">港澳 지원</span><span class="oc-rv">✅</span></div>',
    '<div class="oc-r"><span class="oc-rl">특수상품</span><span class="oc-rv">月卡 포함</span></div>',
    '</div></div>',
    # RORB
    '<div class="oc" style="--gc:#10B981"><div class="oc-code">RORB</div><div class="oc-nm">重生</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">鑽石 (1:1비율)</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">6종</span></div>',
    '<div class="oc-r"><span class="oc-rl">港澳 지원</span><span class="oc-rv">✅</span></div>',
    '</div></div>',
    # ROTL
    '<div class="oc" style="--gc:#F59E0B"><div class="oc-code">ROTL</div><div class="oc-nm">曙光</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">3개 ★제한</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">星石</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">台灣만 5종</span></div>',
    '<div class="oc-r"><span class="oc-rl">港澳 지원</span><span class="oc-rv">❌ 미지원</span></div>',
    '<div class="oc-r"><span class="oc-rl">서버접두어</span><span class="oc-rv">별도 선택 필요</span></div>',
    '</div></div>',
    '</div>', # .ov
]

# Channel support table
lines += [
    '<div class="st">📋 결제 채널 지원 현황 비교표</div>',
    '<div class="tw"><table>',
    '<thead><tr><th>결제 방식</th><th>채널</th>',
    '<th style="color:#FF8CA0">ROBA</th><th style="color:#93C5FD">ROO</th>',
    '<th style="color:#6EE7B7">RORB</th><th style="color:#FCD34D">ROTL</th></tr></thead>',
    '<tbody>',
    '<tr><td rowspan="2"><b>🃏 點數卡</b></td><td>MyCard 點數卡</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td></tr>',
    '<tr><td>GASH 點數卡 (台灣/港澳)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅ 台灣만</td></tr>',
    '<tr><td rowspan="2"><b>💳 信用卡</b></td><td>台灣信用卡 3D</td><td class="tdy">✅ 4종</td><td class="tdy">✅ 16종</td><td class="tdy">✅ 6종</td><td class="tdy">✅ 5종</td></tr>',
    '<tr><td>港澳信用卡 3D</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="2"><b>👛 會員扣點</b></td><td>GASH 錢包 台灣</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>GASH 錢包 港澳</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>📱 行動支付</b></td><td>Apple Pay</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>街口支付 / Google Pay</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>LINE Pay</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>🏦 港澳其他</b></td><td>AlipayHK</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>WeChat Pay</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>PayMe (HSBC)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>📞 電信小額</b></td><td>中華電信 QR (QR839)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>遠傳電信 (FET)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>台哥大 myFone (TCC)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td><b>☎️ 市話HiNet</b></td><td>中華電信 HiNet</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td><b>🏧 WebATM</b></td><td>WebATM 즉시이체</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '</tbody></table></div>',
]

# Credit card amounts comparison table
lines += [
    '<div class="st">💰 신용카드 금액 완전 비교표 (실계정 직접 확인)</div>',
    '<div class="tw"><table>',
    '<thead><tr><th>금액 (TWD)</th>',
    '<th style="color:#FF8CA0">ROBA 彩鑽</th>',
    '<th style="color:#93C5FD">ROO 喵喵果實</th>',
    '<th style="color:#6EE7B7">RORB 鑽石</th>',
    '<th style="color:#FCD34D">ROTL 星石</th></tr></thead>',
    '<tbody>',
    '<tr><td>30</td><td class="tdn">-</td><td class="tdy">✅ 39과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>50</td><td class="tdn">-</td><td class="tdy">✅ 65과실</td><td class="tdy">✅ 50鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>60</td><td class="tdy">✅</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅</td></tr>',
    '<tr><td>150</td><td class="tdn">-</td><td class="tdy">✅ 200과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>250</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 250鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>290</td><td class="tdy">✅</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅</td></tr>',
    '<tr><td>300</td><td class="tdn">-</td><td class="tdy">✅ 400과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>400</td><td class="tdn">-</td><td class="tdy">✅ 530과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>450</td><td class="tdn">-</td><td class="tdy">✅ 600과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>500</td><td class="tdn">-</td><td class="tdy">✅ 680과실</td><td class="tdy">✅ 500鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>750</td><td class="tdn">-</td><td class="tdy">✅ 1,020과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>980</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅</td></tr>',
    '<tr><td>1,000</td><td class="tdn">-</td><td class="tdy">✅ 1,400과실</td><td class="tdy">✅ 1,000鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>1,490</td><td class="tdy">✅</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅</td></tr>',
    '<tr><td>2,000</td><td class="tdn">-</td><td class="tdy">✅ 2,850과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>2,500</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 2,500鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>2,990</td><td class="tdy">✅</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅</td></tr>',
    '<tr><td>3,000</td><td class="tdn">-</td><td class="tdy">✅ 4,350과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>5,000</td><td class="tdn">-</td><td class="tdy">✅ 7,500과실</td><td class="tdy">✅ 5,000鑽石</td><td class="tdn">-</td></tr>',
    '<tr><td>10,000</td><td class="tdn">-</td><td class="tdy">✅ 15,000과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>30,000</td><td class="tdn">-</td><td class="tdy">✅ 45,000과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>50,000</td><td class="tdn">-</td><td class="tdy">✅ 75,000과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>100,000</td><td class="tdn">-</td><td class="tdy">✅ 150,000과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '</tbody></table></div>',
    '</div>', # #ov
]

def cc(color, icon, name, sub, amounts_label, amounts, note='', note_type='ni'):
    """Build a channel card"""
    chips = ''.join(f'<span class="ac">{a}</span>' for a in amounts)
    note_html = f'<div class="{note_type}">{note}</div>' if note else ''
    return (
        f'<div class="cc" style="--cc:{color}">'
        f'<div class="ch"><div class="ci">{icon}</div>'
        f'<div><div class="cn">{name}</div><div class="cs">{sub}</div></div></div>'
        f'<div class="cb"><div class="al">{amounts_label}</div>'
        f'<div class="ag">{chips}</div>{note_html}</div></div>'
    )

def game_section(gid, color, badge_color, code, title, subtitle, tags, notice_html, tabs_html, panels_html):
    badge_style = f'style="background:{badge_color}"' if badge_color else ''
    return (
        f'<div id="{gid}" class="sec">'
        f'<div class="gh" style="--gc:{color}">'
        f'<div class="gb" {badge_style}>{code}</div>'
        f'<div class="gt"><h2>{title}</h2><p>{subtitle}</p></div>'
        f'<div class="gm">{"".join(f"""<span class="mt">{t}</span>""" for t in tags)}</div>'
        f'</div>'
        f'{notice_html}'
        f'<div class="pts">{tabs_html}</div>'
        f'{panels_html}'
        f'</div>'
    )

# === ROBA ===
roba_tabs = (
    '<button class="pt active" onclick="sT(event,\'roba\',\'card\')">🃏 點數卡</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'credit\')">💳 信用卡</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ew\')">👛 會員扣點</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'mob\')">📱 行動支付</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'oth\')">🏦 港澳其他</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ph\')">📞 電信小額</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ph2\')">☎️ 市話HiNet</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'atm\')">🏧 WebATM</button>'
)
roba_panels = (
    f'<div id="roba-card" class="pp active"><div class="cg">'
    + cc('#E65C3F','🃏','MyCard 點數卡','카드번호+비밀번호 직접입력','면액 (TWD)',['100','200','300','500','1,000','2,000'],'실제 지급 彩鑽 수량은 별도 환율표 적용')
    + cc('#F97316','🟠','GASH 點數卡 (台灣)','台灣 지역 GASH 포인트카드','면액 (TWD)',['50','100','200','300','500','1,000'],'台灣 지역 선택 후 GASH 카드번호 입력')
    + cc('#D97706','🟡','GASH 點數卡 (港澳)','港澳 지역 GASH 포인트카드','면액 (HKD)',['50','100','300','500','1,000','2,000'],'⚠️ ROBA 이벤트 기간 중 5,000 면액 임시 숨김 가능','nw')
    + '</div></div>'
    + f'<div id="roba-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','台灣信用卡 3D','VISA/MasterCard 台灣 발행 · 실계정 확인','면액 (TWD) ✅ 실계정 확인',['60','290','1,490','2,990'],'3D 보안인증(OTP) 필수')
    + cc('#7C3AED','💜','港澳信用卡 3D','VISA/MasterCard 港澳 발행','면액 (TWD 환산)',['60','290','1,490','2,990'],'港澳 지역 카드 결제. 환율 자동 적용')
    + '</div></div>'
    + f'<div id="roba-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 錢包扣點 (台灣)','GASH 플랫폼 보유 포인트 차감','면액 (GASH포인트 TWD)',['50','100','200','500','1,000'])
    + cc('#0D9488','🌏','GASH 錢包扣點 (港澳)','港澳 GASH 계정 포인트 차감','면액 (GASH포인트 HKD)',['50','100','300','500'])
    + '</div></div>'
    + f'<div id="roba-mob" class="pp"><div class="cg">'
    + cc('#0EA5E9','🍎','Apple Pay','iOS Safari 전용','면액 (TWD)',['60','290','1,490','2,990'],'⚠️ 모바일 Safari 팝업 차단 해제 필요','nw')
    + cc('#16A34A','🤖','街口支付 / Google Pay','Android / 街口 전자지갑','면액 (TWD)',['60','290','1,490','2,990'])
    + cc('#00B900','💚','LINE Pay','LINE 페이 전자결제','면액 (TWD)',['60','290','1,490','2,990'])
    + '</div></div>'
    + f'<div id="roba-oth" class="pp"><div class="cg">'
    + cc('#1677FF','💙','AlipayHK','香港 알리페이 (港澳 전용)','면액 (HKD)',['30','60','150','300','600'])
    + cc('#07C160','💬','WeChat Pay','微信支付 (港澳 전용)','면액 (HKD)',['30','60','150','300'])
    + cc('#E31837','🏦','PayMe (HSBC)','홍콩 HSBC PayMe','면액 (HKD)',['30','60','150','300'])
    + '</div></div>'
    + f'<div id="roba-ph" class="pp"><div class="cg">'
    + cc('#0070C9','📡','中華電信 QR (QR839)','CHT 통신 소액결제 QR','면액 (TWD)',['30','50','100','150','200','250','300','350','400','450','500'],'⚠️ 3,000 TWD 이상 단건 또는 30일 누적 5,000 이상 시 MID 본인인증 필요','nw')
    + cc('#FF6600','📶','遠傳電信 (FET)','Far EasTone 통신 소액결제','면액 (TWD)',['30','50','100','150','200','250','300','500'])
    + cc('#CC0000','📱','台哥大 myFone (TCC)','Taiwan Mobile 통신 소액결제','면액 (TWD)',['30','50','100','150','200','250','300','500'])
    + '</div></div>'
    + f'<div id="roba-ph2" class="pp"><div class="cg">'
    + cc('#005BAA','☎️','中華電信 HiNet 市話','유선전화 HiNet 요금 합산 결제','면액 (TWD)',['100','200','300','500'],'유선전화 번호 입력 필요. HiNet 가입자 전용')
    + '</div></div>'
    + f'<div id="roba-atm" class="pp"><div class="cg">'
    + cc('#374151','🏧','WebATM 即時轉帳','대만 은행 WebATM 인터넷 뱅킹','면액 (TWD)',['100','300','500','1,000','2,000','3,000','5,000'],'대만 은행 계좌 + WebATM 기기 또는 공인인증 필요')
    + '</div></div>'
)

roba_notice = (
    '<div class="ntc" style="background:rgba(200,16,46,.06);border:1px solid rgba(200,16,46,.2);color:#FCA5A5;">'
    '<h4 style="color:#FF8CA0">⚠️ ROBA 결제 주의사항</h4><ul>'
    '<li>ROBA는 특정 이벤트 기간 중 <b>港澳(HK/Macau) 5,000 면액</b>이 임시 숨김 처리될 수 있음 (billingNew.js 코드 확인)</li>'
    '<li>MyCard 점수카드 선택 시 카드번호(序號)와 비밀번호(密碼)를 직접 입력해야 함</li>'
    '<li>電信小額付費 선택 시 인증된 휴대폰 번호 필요. 3,000 TWD 이상 단건 또는 30일 누적 5,000 TWD 이상 시 MID 본인인증 필요</li>'
    '</ul></div>'
)

lines.append(game_section(
    'roba', '#C8102E', None, 'ROBA',
    'RO 仙境傳說：初心之戰',
    '게임화폐: 彩鑽 (색다이아) · 서버+캐릭터 선택 필요',
    ['결제 탭 <b>8개</b>', '신용카드 면액 <b>4종</b>', '港澳 <b>지원</b>'],
    roba_notice, roba_tabs, roba_panels
))

# === ROO ===
roo_tabs = (
    '<button class="pt active" onclick="sT(event,\'roo\',\'card\')">🃏 點數卡</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'credit\')">💳 信用卡</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ew\')">👛 會員扣點</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'mob\')">📱 行動支付</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'oth\')">🏦 港澳其他</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ph\')">📞 電信小額</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ph2\')">☎️ 市話HiNet</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'atm\')">🏧 WebATM</button>'
)
roo_panels = (
    f'<div id="roo-card" class="pp active"><div class="cg">'
    + cc('#E65C3F','🃏','MyCard 點數卡','카드번호+비밀번호 직접입력','면액 (TWD)',['100','200','300','500','1,000'])
    + cc('#F97316','🟠','GASH 點數卡 (台灣/港澳)','台灣 · 港澳 지역 선택','면액 (TWD)',['50','100','300','500','1,000'])
    + '</div></div>'
    + f'<div id="roo-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','台灣信用卡 3D','VISA/MasterCard 台灣 발행 · ✅ 실계정 직접 확인 완료','면액(TWD) → 喵喵果實 지급량 ✅ 실계정 확인',
         ['30','50','150','300','400','450','500','750','1,000','2,000','3,000','5,000','10,000','30,000','50,000','100,000'],
         '30→39 / 50→65 / 150→200 / 300→400 / 400→530 / 450→600 / 500→680 / 750→1,020 / 1,000→1,400 / 2,000→2,850 / 3,000→4,350 / 5,000→7,500 / 10,000→15,000 / 30,000→45,000 / 50,000→75,000 / 100,000→150,000 과실')
    + cc('#7C3AED','💜','港澳信用卡 3D','VISA/MasterCard 港澳 발행','면액 (HKD 환산 자동)',['30','50','150','300','450','500','750','1,000','2,000','3,000','5,000'])
    + '</div></div>'
    + f'<div id="roo-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 錢包扣點 (台灣/港澳)','GASH 플랫폼 보유 포인트 차감','면액 (GASH포인트)',['50','100','200','500','1,000'])
    + '</div></div>'
    + f'<div id="roo-mob" class="pp"><div class="cg">'
    + cc('#0EA5E9','🍎','Apple Pay','iOS Safari 전용','면액 (TWD)',['50','150','300','500','1,000'],'⚠️ 모바일 Safari 팝업 차단 해제 필요','nw')
    + cc('#16A34A','🤖','街口支付 / Google Pay','Android 전자지갑','면액 (TWD)',['50','150','300','500'])
    + cc('#00B900','💚','LINE Pay','LINE 페이 결제','면액 (TWD)',['50','150','300','500'])
    + '</div></div>'
    + f'<div id="roo-oth" class="pp"><div class="cg">'
    + cc('#1677FF','💙','AlipayHK','港澳 전용','면액 (HKD)',['30','60','150','300'])
    + cc('#07C160','💬','WeChat Pay','港澳 전용','면액 (HKD)',['30','60','150','300'])
    + cc('#E31837','🏦','PayMe (HSBC)','홍콩 HSBC','면액 (HKD)',['30','60','150'])
    + '</div></div>'
    + f'<div id="roo-ph" class="pp"><div class="cg">'
    + cc('#0070C9','📡','中華電信 QR (QR839)','CHT 통신 소액결제','면액 (TWD)',['30','50','100','150','200','300','500'],'⚠️ MID 본인인증: 3,000 TWD 이상 단건 또는 30일 누적 5,000 이상','nw')
    + cc('#FF6600','📶','遠傳電信 (FET)','Far EasTone','면액 (TWD)',['30','50','100','200','300','500'])
    + cc('#CC0000','📱','台哥大 myFone (TCC)','Taiwan Mobile','면액 (TWD)',['30','50','100','200','300','500'])
    + '</div></div>'
    + f'<div id="roo-ph2" class="pp"><div class="cg">'
    + cc('#005BAA','☎️','中華電信 HiNet 市話','유선전화 요금 합산','면액 (TWD)',['100','200','300','500'])
    + '</div></div>'
    + f'<div id="roo-atm" class="pp"><div class="cg">'
    + cc('#374151','🏧','WebATM 即時轉帳','대만 은행 인터넷 뱅킹','면액 (TWD)',['100','300','500','1,000','3,000','5,000'])
    + '</div></div>'
)
roo_notice = (
    '<div class="ntc" style="background:rgba(59,130,246,.06);border:1px solid rgba(59,130,246,.25);color:#BFDBFE;">'
    '<h4 style="color:#93C5FD">ℹ️ ROO 결제 특이사항</h4><ul>'
    '<li>喵喵果實이 가장 세분화 — 신용카드 기준 <b>30 TWD ~ 100,000 TWD</b> 16단계</li>'
    '<li>일부 상품은 "月卡(월카드)" 형태로 첫구매/재구매에 따라 과실 수량이 달라짐</li>'
    '<li>신용카드 기준 <b>최대 100,000 TWD</b> 단건 결제 지원 (ROBA·RORB 대비 압도적)</li>'
    '</ul></div>'
)
lines.append(game_section(
    'roo', '#3B82F6', '#3B82F6', 'ROO',
    'RO 仙境傳說：愛如初見',
    '게임화폐: 喵喵果實 (냥과실) · 서버+캐릭터 선택 필요 · 가장 많은 면액 구성',
    ['결제 탭 <b>8개</b>', '신용카드 면액 <b>16종 ★최다</b>', '月卡 <b>포함</b>', '최대 <b>100,000 TWD</b>'],
    roo_notice, roo_tabs, roo_panels
))

# === RORB ===
rorb_tabs = (
    '<button class="pt active" onclick="sT(event,\'rorb\',\'card\')">🃏 點數卡</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'credit\')">💳 信用卡</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ew\')">👛 會員扣點</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'mob\')">📱 行動支付</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'oth\')">🏦 港澳其他</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ph\')">📞 電信小額</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ph2\')">☎️ 市話HiNet</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'atm\')">🏧 WebATM</button>'
)
rorb_panels = (
    f'<div id="rorb-card" class="pp active"><div class="cg">'
    + cc('#E65C3F','🃏','MyCard 點數卡','카드번호+비밀번호 직접입력','면액 (TWD)',['100','200','500','1,000'])
    + cc('#F97316','🟠','GASH 點數卡 (台灣/港澳)','台灣 · 港澳 지역 선택','면액 (TWD)',['50','100','200','500','1,000'])
    + '</div></div>'
    + f'<div id="rorb-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','台灣信用卡 3D','VISA/MasterCard 台灣 · ✅ 실계정 확인','면액(TWD) → 鑽石 (1:1 비율) ✅ 실계정 확인',
         ['50','250','500','1,000','2,500','5,000'],
         '50→50鑽石 / 250→250 / 500→500 / 1,000→1,000 / 2,500→2,500 / 5,000→5,000 (완전 1:1 비율)')
    + cc('#7C3AED','💜','港澳信用卡 3D','VISA/MasterCard 港澳 발행','면액 (TWD 동일)',['50','250','500','1,000','2,500','5,000'])
    + '</div></div>'
    + f'<div id="rorb-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 錢包扣點 (台灣/港澳)','GASH 플랫폼 포인트 차감','면액 (GASH포인트)',['50','100','500','1,000'])
    + '</div></div>'
    + f'<div id="rorb-mob" class="pp"><div class="cg">'
    + cc('#0EA5E9','🍎','Apple Pay','iOS Safari 전용','면액 (TWD)',['50','250','500','1,000'],'⚠️ 모바일 Safari 팝업 차단 해제 필요','nw')
    + cc('#16A34A','🤖','街口支付 / Google Pay','Android 전자지갑','면액 (TWD)',['50','250','500'])
    + cc('#00B900','💚','LINE Pay','LINE 페이 결제','면액 (TWD)',['50','250','500'])
    + '</div></div>'
    + f'<div id="rorb-oth" class="pp"><div class="cg">'
    + cc('#1677FF','💙','AlipayHK / WeChat Pay / PayMe','港澳 전용 3개 채널','면액 (HKD)',['30','60','150','300'])
    + '</div></div>'
    + f'<div id="rorb-ph" class="pp"><div class="cg">'
    + cc('#0070C9','📡','中華電信 / 遠傳 / 台哥大','대만 3대 통신사 소액결제','면액 (TWD)',['30','50','100','200','300','500'],'⚠️ 인증된 휴대폰 번호 필요','nw')
    + '</div></div>'
    + f'<div id="rorb-ph2" class="pp"><div class="cg">'
    + cc('#005BAA','☎️','中華電信 HiNet 市話','유선전화 요금 합산','면액 (TWD)',['100','200','300','500'])
    + '</div></div>'
    + f'<div id="rorb-atm" class="pp"><div class="cg">'
    + cc('#374151','🏧','WebATM 即時轉帳','대만 은행 인터넷 뱅킹','면액 (TWD)',['100','300','500','1,000','3,000'])
    + '</div></div>'
)
lines.append(game_section(
    'rorb', '#10B981', '#10B981', 'RORB',
    'RO 仙境傳說：重生',
    '게임화폐: 鑽石 (다이아, 1:1 비율) · 서버+캐릭터 선택 필요 · 단순한 면액 구성',
    ['결제 탭 <b>8개</b>', '신용카드 면액 <b>6종</b>', '게임화폐 <b>1:1 비율</b>'],
    '', rorb_tabs, rorb_panels
))

# === ROTL ===
rotl_tabs = (
    '<button class="pt active" onclick="sT(event,\'rotl\',\'card\')">🃏 點數卡</button>'
    '<button class="pt" onclick="sT(event,\'rotl\',\'credit\')">💳 信用卡 (台灣만)</button>'
    '<button class="pt" onclick="sT(event,\'rotl\',\'mob\')">📱 行動支付</button>'
    '<button class="pt dis">👛 會員扣點 ❌ 미지원</button>'
    '<button class="pt dis">🏦 港澳其他 ❌ 미지원</button>'
    '<button class="pt dis">📞 電信小額 ❌ 미지원</button>'
    '<button class="pt dis">☎️ HiNet ❌ 미지원</button>'
    '<button class="pt dis">🏧 WebATM ❌ 미지원</button>'
)
rotl_notice = (
    '<div class="ntc" style="background:rgba(245,158,11,.06);border:1px solid rgba(245,158,11,.3);color:#FDE68A;">'
    '<h4 style="color:#FCD34D">⚠️ ROTL 결제 제한 사항</h4><ul>'
    '<li>서버 선택 시 <b>서버 접두어(xServerNamePre)</b>를 먼저 선택해야 서버 목록이 나타남 (타 게임과 다름)</li>'
    '<li>결제 채널이 크게 제한됨: <b>點數卡 · 台灣信用卡 · 行動支付(일부)</b> 3개 카테고리만 지원</li>'
    '<li><b>港澳 신용카드, GASH 지갑, 電信소액결제, HiNet 시화, WebATM 전부 미지원</b></li>'
    '<li>信用卡는 <b>台灣 발행 카드만</b> 지원 (港澳 신용카드 없음)</li>'
    '</ul></div>'
)
rotl_panels = (
    f'<div id="rotl-card" class="pp active"><div class="cg">'
    + cc('#E65C3F','🃏','MyCard 點數卡','카드번호+비밀번호 직접입력','면액 (TWD)',['100','200','500','1,000'])
    + cc('#F97316','🟠','GASH 點數卡 (台灣만)','港澳 GASH 카드 미지원','면액 (TWD)',['50','100','200','500'],'⚠️ 台灣 발행 GASH 카드만 지원. 港澳 카드 미지원','nw')
    + '</div></div>'
    + f'<div id="rotl-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','台灣信用卡 3D만','VISA/MasterCard 台灣 발행 · 港澳 카드 사용 불가','면액 (TWD)',['60','290','980','1,490','2,990'],'⚠️ 港澳 신용카드 사용 불가. 台灣 발행 카드만 결제 가능','nw')
    + '</div></div>'
    + f'<div id="rotl-mob" class="pp"><div class="cg">'
    + cc('#0EA5E9','🍎','Apple Pay','iOS Safari 전용 (제한적)','면액 (TWD)',['60','290','1,490'],'⚠️ 지원 여부 Cloudflare Turnstile 캡차로 확인 불완전','nw')
    + '</div></div>'
)
lines.append(game_section(
    'rotl', '#F59E0B', '#F59E0B', 'ROTL',
    'RO 仙境傳說：曙光',
    '게임화폐: 星石 (별돌) · 서버 접두어 별도 선택 필요 · 결제 탭 수 제한',
    ['결제 탭 <b>3개 ★제한</b>', '台灣만 <b>신용카드</b>', '港澳 <b>전면 미지원</b>'],
    rotl_notice, rotl_tabs, rotl_panels
))

# Close wrap + JS
lines += [
    '</div>', # .wrap
    '<script>',
    'function sG(e,id){',
    '  document.querySelectorAll(".sec").forEach(s=>s.classList.remove("active"));',
    '  document.querySelectorAll(".nb").forEach(b=>b.classList.remove("active"));',
    '  document.getElementById(id).classList.add("active");',
    '  e.currentTarget.classList.add("active");',
    '}',
    'function sT(e,g,t){',
    '  document.querySelectorAll("#"+g+" .pp").forEach(p=>p.classList.remove("active"));',
    '  document.querySelectorAll("#"+g+" .pt:not(.dis)").forEach(b=>b.classList.remove("active"));',
    '  var panel=document.getElementById(g+"-"+t);',
    '  if(panel)panel.classList.add("active");',
    '  e.currentTarget.classList.add("active");',
    '}',
    '</script>',
    '</body></html>',
]

output = '\n'.join(lines)
with open('gnjoy_billing_complete_report.html', 'w', encoding='utf-8') as f:
    f.write(output)
print(f'Done! Written {len(output)} chars, {output.count(chr(10))} lines')
