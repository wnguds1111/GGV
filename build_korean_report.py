
import sys

# Build HTML report with full Korean translation for payment methods and channels
lines = [
    '<!DOCTYPE html>',
    '<html lang="ko">',
    '<head>',
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<title>GNJOY HK - 게임별 결제 채널 완전 분석 보고서 (한글판)</title>',
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700;900&display=swap" rel="stylesheet">',
    '<style>',
    ':root{--p:#C8102E;--bg:#F8FAFC;--bgc:#FFFFFF;--bgp:#F1F5F9;--bd:#E2E8F0;--tx:#0F172A;--tm:#64748B;}',
    '*{margin:0;padding:0;box-sizing:border-box;}',
    'body{font-family:"Noto Sans KR",sans-serif;background:var(--bg);color:var(--tx);line-height:1.6;}',
    '.hd{background:linear-gradient(135deg,#C8102E 0%,#8B0A1E 100%);padding:36px 48px 28px;border-bottom:1px solid #B91C1C;box-shadow:0 4px 14px rgba(200,16,46,0.15);}',
    '.hd h1{font-size:26px;font-weight:900;color:#FFFFFF;margin-bottom:10px;text-shadow:0 2px 4px rgba(0,0,0,0.1);}',
    '.hd-sub{display:flex;gap:12px;flex-wrap:wrap;}',
    '.hd-chip{background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.3);border-radius:6px;padding:4px 14px;font-size:11px;color:#FFFFFF;}',
    '.hd-chip b{color:#FFFFFF;font-weight:700;}',
    '.nav{background:#FFFFFF;border-bottom:1px solid var(--bd);padding:0 48px;display:flex;overflow-x:auto;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,.05);}',
    '.nb{padding:15px 22px;background:none;border:none;border-bottom:3px solid transparent;color:var(--tm);font-size:13px;font-weight:600;cursor:pointer;white-space:nowrap;transition:.2s;font-family:inherit;}',
    '.nb:hover{color:var(--tx);background:#F8FAFC;}',
    '.nb.active{color:var(--p);border-bottom-color:var(--p);font-weight:700;}',
    '.wrap{max-width:1600px;margin:0 auto;padding:36px 48px;}',
    '.sec{display:none;}.sec.active{display:block;}',
    '.gh{display:flex;align-items:center;gap:18px;margin-bottom:28px;padding:22px 26px;background:#FFFFFF;border-radius:14px;border:1px solid var(--bd);position:relative;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.03);}',
    '.gh::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;background:var(--gc,var(--p));}',
    '.gb{background:var(--gc,var(--p));color:#fff;font-size:13px;font-weight:800;padding:5px 13px;border-radius:7px;flex-shrink:0;}',
    '.gt h2{font-size:20px;font-weight:800;margin-bottom:3px;color:var(--tx);}',
    '.gt p{font-size:12px;color:var(--tm);}',
    '.gm{display:flex;gap:8px;flex-wrap:wrap;}',
    '.mt{background:#F1F5F9;border:1px solid var(--bd);border-radius:5px;padding:3px 10px;font-size:11px;color:var(--tm);}',
    '.mt b{color:var(--tx);}',
    '.ntc{border-radius:10px;padding:14px 18px;margin-bottom:22px;font-size:12.5px;}',
    '.ntc h4{font-size:13px;font-weight:700;margin-bottom:7px;}',
    '.ntc ul{padding-left:15px;}.ntc li{margin-bottom:3px;}',
    '.pts{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:22px;}',
    '.pt{padding:7px 16px;background:#FFFFFF;border:1px solid var(--bd);border-radius:7px;color:var(--tm);font-size:12px;font-weight:600;cursor:pointer;transition:.2s;font-family:inherit;box-shadow:0 1px 3px rgba(0,0,0,.03);}',
    '.pt:hover{border-color:var(--p);color:var(--tx);}',
    '.pt.active{background:var(--p);border-color:var(--p);color:#fff;font-weight:700;box-shadow:0 2px 6px rgba(200,16,46,.25);}',
    '.pt.dis{opacity:.4;cursor:not-allowed;background:#F1F5F9;}',
    '.pp{display:none;}.pp.active{display:block;}',
    '.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:18px;margin-bottom:22px;}',
    '.cc{background:#FFFFFF;border:1px solid var(--bd);border-radius:13px;overflow:hidden;transition:.2s;box-shadow:0 2px 6px rgba(0,0,0,.03);}',
    '.cc:hover{border-color:var(--cc,var(--p));box-shadow:0 6px 16px rgba(0,0,0,.08);transform:translateY(-2px);}',
    '.ch{background:var(--cc,var(--p));padding:13px 16px;display:flex;align-items:center;gap:9px;}',
    '.ci{width:34px;height:34px;background:rgba(255,255,255,.25);border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}',
    '.cn{font-size:14px;font-weight:700;color:#FFFFFF;}',
    '.cs{font-size:11px;color:rgba(255,255,255,.9);margin-top:1px;}',
    '.cb{padding:16px;background:#FFFFFF;}',
    '.al{font-size:10px;font-weight:700;color:var(--tm);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;}',
    '.ag{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px;}',
    '.ac{background:#F1F5F9;border:1px solid #CBD5E1;border-radius:6px;padding:3px 9px;font-size:13px;font-weight:700;color:#1E293B;}',
    '.nw{background:#FFFBEB;border:1px solid #FDE68A;border-radius:7px;padding:9px 12px;font-size:11.5px;color:#B45309;margin-top:8px;}',
    '.ni{background:#EFF6FF;border:1px solid #BFDBFE;border-radius:7px;padding:9px 12px;font-size:11.5px;color:#1E40AF;margin-top:8px;}',
    '.st{font-size:17px;font-weight:800;margin-bottom:18px;display:flex;align-items:center;gap:10px;color:var(--tx);}',
    '.st::after{content:"";flex:1;height:1px;background:var(--bd);}',
    '.tw{overflow-x:auto;border-radius:13px;border:1px solid var(--bd);margin-bottom:30px;background:#FFFFFF;box-shadow:0 2px 6px rgba(0,0,0,.03);}',
    'table{width:100%;border-collapse:collapse;font-size:13px;}',
    'th{background:#F8FAFC;padding:13px 14px;text-align:left;font-weight:700;color:#475569;border-bottom:1px solid var(--bd);white-space:nowrap;}',
    'td{padding:11px 14px;border-bottom:1px solid #F1F5F9;vertical-align:top;color:#334155;}',
    'tr:last-child td{border-bottom:none;}',
    'tr:hover td{background:#F8FAFC;}',
    '.tdy{color:#059669;font-weight:700;}',
    '.tdn{color:#94A3B8;}',
    '.ov{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:36px;}',
    '.oc{background:#FFFFFF;border:1px solid var(--bd);border-radius:13px;padding:18px;position:relative;overflow:hidden;transition:.2s;box-shadow:0 2px 6px rgba(0,0,0,.03);}',
    '.oc:hover{border-color:var(--gc,var(--p));transform:translateY(-2px);box-shadow:0 6px 16px rgba(0,0,0,.06);}',
    '.oc::before{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:var(--gc,var(--p));}',
    '.oc-code{font-size:10px;font-weight:700;letter-spacing:2px;color:var(--tm);text-transform:uppercase;margin-bottom:5px;}',
    '.oc-nm{font-size:15px;font-weight:800;margin-bottom:10px;color:var(--tx);}',
    '.oc-s{display:flex;flex-direction:column;gap:4px;}',
    '.oc-r{display:flex;justify-content:space-between;font-size:11.5px;}',
    '.oc-rl{color:var(--tm);}',
    '.oc-rv{font-weight:700;color:var(--tx);}',
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
    '<span class="hd-chip">결제 카테고리 <b>8개 (한국어 변환)</b></span>',
    '<span class="hd-chip">수집방법 <b>실계정 브라우저 직접클릭</b></span>',
    '<span class="hd-chip">ROO 금액 <b>실계정 직접 확인 완료</b></span>',
    '<span class="hd-chip">날짜 <b>2026-08-03</b></span>',
    '</div></div>',
]

# NAV
lines += [
    '<div class="nav">',
    '<button class="nb active" onclick="sG(event,\'ov\')">📊 전체 비교</button>',
    '<button class="nb" onclick="sG(event,\'roba\')">🔴 ROBA 초심지전 (初心之戰)</button>',
    '<button class="nb" onclick="sG(event,\'roo\')">🔵 ROO 여여초견 (愛如初見)</button>',
    '<button class="nb" onclick="sG(event,\'rorb\')">🟢 RORB 중생 (重生)</button>',
    '<button class="nb" onclick="sG(event,\'rotl\')">🟡 ROTL 서광 (曙光)</button>',
    '</div>',
    '<div class="wrap">',
]

# === OVERVIEW SECTION ===
lines += [
    '<div id="ov" class="sec active">',
    '<div class="st">🎯 게임별 결제 인프라 요약</div>',
    '<div class="ov">',
    # ROBA
    '<div class="oc" style="--gc:#C8102E"><div class="oc-code">ROBA</div><div class="oc-nm">초심지전 (初心之戰)</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">색다이아 (彩鑽)</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">4종</span></div>',
    '<div class="oc-r"><span class="oc-rl">홍콩/마카오 지원</span><span class="oc-rv">✅</span></div>',
    '</div></div>',
    # ROO
    '<div class="oc" style="--gc:#2563EB"><div class="oc-code">ROO</div><div class="oc-nm">여여초견 (愛如初見)</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">냥과실 (喵喵果實)</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">16종 ★최다</span></div>',
    '<div class="oc-r"><span class="oc-rl">홍콩/마카오 지원</span><span class="oc-rv">✅</span></div>',
    '<div class="oc-r"><span class="oc-rl">특수상품</span><span class="oc-rv">월카드(月卡) 포함</span></div>',
    '</div></div>',
    # RORB
    '<div class="oc" style="--gc:#059669"><div class="oc-code">RORB</div><div class="oc-nm">중생 (重生)</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">8개</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">다이아 (鑽石 1:1)</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">6종</span></div>',
    '<div class="oc-r"><span class="oc-rl">홍콩/마카오 지원</span><span class="oc-rv">✅</span></div>',
    '</div></div>',
    # ROTL
    '<div class="oc" style="--gc:#D97706"><div class="oc-code">ROTL</div><div class="oc-nm">서광 (曙光)</div><div class="oc-s">',
    '<div class="oc-r"><span class="oc-rl">결제 탭</span><span class="oc-rv">3개 ★제한</span></div>',
    '<div class="oc-r"><span class="oc-rl">게임화폐</span><span class="oc-rv">별돌 (星石)</span></div>',
    '<div class="oc-r"><span class="oc-rl">신용카드 면액</span><span class="oc-rv">대만 전용 5종</span></div>',
    '<div class="oc-r"><span class="oc-rl">홍콩/마카오 지원</span><span class="oc-rv">❌ 미지원</span></div>',
    '<div class="oc-r"><span class="oc-rl">서버접두어</span><span class="oc-rv">별도 선택 필요</span></div>',
    '</div></div>',
    '</div>', # .ov
]

# Channel support table (Translated to Korean)
lines += [
    '<div class="st">📋 결제 채널 지원 현황 비교표 (한국어 카테고리)</div>',
    '<div class="tw"><table>',
    '<thead><tr><th>결제 방식 (한국어)</th><th>세부 채널 (PG / 수단)</th>',
    '<th style="color:#C8102E">ROBA</th><th style="color:#2563EB">ROO</th>',
    '<th style="color:#059669">RORB</th><th style="color:#D97706">ROTL</th></tr></thead>',
    '<tbody>',
    '<tr><td rowspan="2"><b>🃏 포인트 카드 (點數卡)</b></td><td>MyCard 포인트 카드 (MyCard點數卡)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td></tr>',
    '<tr><td>GASH 포인트 카드 (대만/홍콩 GASH點數卡)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅ 대만만</td></tr>',
    '<tr><td rowspan="2"><b>💳 신용카드 (信用卡)</b></td><td>대만 신용카드 3D 보안결제 (台灣信用卡3D)</td><td class="tdy">✅ 4종</td><td class="tdy">✅ 16종</td><td class="tdy">✅ 6종</td><td class="tdy">✅ 5종</td></tr>',
    '<tr><td>홍콩/마카오 신용카드 3D (港澳信用卡3D)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="2"><b>👛 회원 포인트 차감 (會員扣點)</b></td><td>GASH 전자지갑 대만 (GASH錢包 台灣)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>GASH 전자지갑 홍콩 (GASH錢包 港澳)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>📱 모바일 간편결제 (行動支付)</b></td><td>Apple Pay (애플페이)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>JKOPAY / Google Pay (지구페이/구글페이)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>LINE Pay (라인페이)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>🏦 홍콩/마카오 결제 (港澳其他付費)</b></td><td>AlipayHK (홍콩 알리페이)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>WeChat Pay (위챗페이 HK)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>PayMe (HSBC 페이미)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td rowspan="3"><b>📞 통신사 소액결제 (電信小額付費)</b></td><td>중화전신 소액결제 (中華電信 QR839)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>원전전신 소액결제 (遠傳電信 FET)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td>타이완모바일 소액결제 (台哥大 myFone TCC)</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td><b>☎️ 유선전화 결제 (市話HiNet)</b></td><td>중화전신 HiNet 유선전화 요금합산</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '<tr><td><b>🏧 WebATM 실시간 이체 (WebATM)</b></td><td>대만 주요 은행 WebATM 계좌이체</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdy">✅</td><td class="tdn">❌</td></tr>',
    '</tbody></table></div>',
]

# Credit card amounts comparison table
lines += [
    '<div class="st">💰 신용카드 금액 완전 비교표 (실계정 직접 확인)</div>',
    '<div class="tw"><table>',
    '<thead><tr><th>결제 금액 (TWD 대만달러)</th>',
    '<th style="color:#C8102E">ROBA 색다이아 (彩鑽)</th>',
    '<th style="color:#2563EB">ROO 냥과실 (喵喵果實)</th>',
    '<th style="color:#059669">RORB 다이아 (鑽石)</th>',
    '<th style="color:#D97706">ROTL 별돌 (星石)</th></tr></thead>',
    '<tbody>',
    '<tr><td>30 TWD</td><td class="tdn">-</td><td class="tdy">✅ 39 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>50 TWD</td><td class="tdn">-</td><td class="tdy">✅ 65 냥과실</td><td class="tdy">✅ 50 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>60 TWD</td><td class="tdy">✅ 지원</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 지원</td></tr>',
    '<tr><td>150 TWD</td><td class="tdn">-</td><td class="tdy">✅ 200 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>250 TWD</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 250 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>290 TWD</td><td class="tdy">✅ 지원</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 지원</td></tr>',
    '<tr><td>300 TWD</td><td class="tdn">-</td><td class="tdy">✅ 400 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>400 TWD</td><td class="tdn">-</td><td class="tdy">✅ 530 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>450 TWD</td><td class="tdn">-</td><td class="tdy">✅ 600 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>500 TWD</td><td class="tdn">-</td><td class="tdy">✅ 680 냥과실</td><td class="tdy">✅ 500 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>750 TWD</td><td class="tdn">-</td><td class="tdy">✅ 1,020 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>980 TWD</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 지원</td></tr>',
    '<tr><td>1,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 1,400 냥과실</td><td class="tdy">✅ 1,000 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>1,490 TWD</td><td class="tdy">✅ 지원</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 지원</td></tr>',
    '<tr><td>2,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 2,850 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>2,500 TWD</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 2,500 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>2,990 TWD</td><td class="tdy">✅ 지원</td><td class="tdn">-</td><td class="tdn">-</td><td class="tdy">✅ 지원</td></tr>',
    '<tr><td>3,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 4,350 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>5,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 7,500 냥과실</td><td class="tdy">✅ 5,000 다이아 (1:1)</td><td class="tdn">-</td></tr>',
    '<tr><td>10,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 15,000 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>30,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 45,000 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>50,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 75,000 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
    '<tr><td>100,000 TWD</td><td class="tdn">-</td><td class="tdy">✅ 150,000 냥과실</td><td class="tdn">-</td><td class="tdn">-</td></tr>',
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

# Korean tab buttons for game view
korean_game_tabs = (
    '<button class="pt active" onclick="sT(event,\'{gid}\',\'card\')">🃏 포인트 카드</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'credit\')">💳 신용카드</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'ew\')">👛 회원 포인트 차감</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'mob\')">📱 모바일 간편결제</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'oth\')">🏦 홍콩/마카오 결제</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'ph\')">📞 통신사 소액결제</button>'
    '<button class="pt" onclick="sT(event,\'{gid}\',\'ph2\')">☎️ 유선전화 HiNet</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'atm\')">🏧 WebATM 계좌이체</button>'
)

# === ROBA ===
roba_tabs = (
    '<button class="pt active" onclick="sT(event,\'roba\',\'card\')">🃏 포인트 카드</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'credit\')">💳 신용카드</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ew\')">👛 회원 포인트 차감</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'mob\')">📱 모바일 간편결제</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'oth\')">🏦 홍콩/마카오 결제</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ph\')">📞 통신사 소액결제</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'ph2\')">☎️ 유선전화 HiNet</button>'
    '<button class="pt" onclick="sT(event,\'roba\',\'atm\')">🏧 WebATM 계좌이체</button>'
)
roba_panels = (
    f'<div id="roba-card" class="pp active"><div class="cg">'
    + cc('#C8102E','🃏','MyCard 포인트 카드 (MyCard點數卡)','카드 일련번호 및 비밀번호 직접 입력 방식','충전 면액 (TWD 대만달러)',['100','200','300','500','1,000','2,000'],'실제 지급되는 색다이아(彩鑽) 수량은 환율표 적용')
    + cc('#EA580C','🟠','GASH 포인트 카드 대만 (GASH點數卡 台灣)','대만 지역 발행 GASH 선불 카드','충전 면액 (TWD 대만달러)',['50','100','200','300','500','1,000'],'대만 지역 선택 후 GASH 핀번호 입력')
    + cc('#D97706','🟡','GASH 포인트 카드 홍콩 (GASH點數卡 港澳)','홍콩/마카오 지역 발행 GASH 카드','충전 면액 (HKD 홍콩달러)',['50','100','300','500','1,000','2,000'],'⚠️ ROBA 특정 이벤트 기간 중 5,000 면액 임시 숨김 처리 가능','nw')
    + '</div></div>'
    + f'<div id="roba-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','대만 신용카드 (台灣信用卡 3D)','VISA / MasterCard 대만 발행 카드 · 실계정 확인 완료','충전 면액 (TWD 대만달러)',['60','290','1,490','2,990'],'3D 보안인증 (OTP 핀코드) 필수')
    + cc('#7D5265','💜','홍콩/마카오 신용카드 (港澳信用卡 3D)','VISA / MasterCard 홍콩/마카오 발행 카드','충전 면액 (TWD 환산)',['60','290','1,490','2,990'],'홍콩/마카오 해외 발행 카드 전용. 자동 환율 적용')
    + '</div></div>'
    + f'<div id="roba-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 전자지갑 대만 (GASH錢包 台灣)','GASH 대만 회원 계정 보유 포인트 차감','충전 면액 (GASH 포인트 TWD)',['50','100','200','500','1,000'])
    + cc('#0D9488','🌏','GASH 전자지갑 홍콩 (GASH錢包 港澳)','GASH 홍콩 회원 계정 보유 포인트 차감','충전 면액 (GASH 포인트 HKD)',['50','100','300','500'])
    + '</div></div>'
    + f'<div id="roba-mob" class="pp"><div class="cg">'
    + cc('#0284C7','🍎','Apple Pay (애플페이)','iOS Safari 모바일 브라우저 전용','충전 면액 (TWD 대만달러)',['60','290','1,490','2,990'],'⚠️ 모바일 Safari 팝업 차단 해제 필수','nw')
    + cc('#16A34A','🤖','지구페이 / 구글페이 (街口支付 / Google Pay)','Android 및 대만 1위 모바일 전자지갑','충전 면액 (TWD 대만달러)',['60','290','1,490','2,990'])
    + cc('#16A34A','💚','LINE Pay (라인페이)','LINE Pay 대만 모바일 간편결제','충전 면액 (TWD 대만달러)',['60','290','1,490','2,990'])
    + '</div></div>'
    + f'<div id="roba-oth" class="pp"><div class="cg">'
    + cc('#2563EB','💙','AlipayHK (홍콩 알리페이)','홍콩 알리페이 (홍콩/마카오 지역 전용)','충전 면액 (HKD 홍콩달러)',['30','60','150','300','600'])
    + cc('#059669','💬','WeChat Pay (위챗페이 HK)','홍콩 위챗페이 (홍콩/마카오 지역 전용)','충전 면액 (HKD 홍콩달러)',['30','60','150','300'])
    + cc('#DC2626','🏦','PayMe (HSBC 페이미)','홍콩 HSBC PayMe 모바일 결제','충전 면액 (HKD 홍콩달러)',['30','60','150','300'])
    + '</div></div>'
    + f'<div id="roba-ph" class="pp"><div class="cg">'
    + cc('#0284C7','📡','중화전신 소액결제 (中華電信 QR839)','대만 1위 중화전신 통신사 소액결제 QR','충전 면액 (TWD 대만달러)',['30','50','100','150','200','250','300','350','400','450','500'],'⚠️ 3,000 TWD 이상 단건 또는 30일 누적 5,000 이상 결제 시 MID 본인인증 진행','nw')
    + cc('#EA580C','📶','원전전신 소액결제 (遠傳電信 FET)','대만 Far EasTone 통신 소액결제','충전 면액 (TWD 대만달러)',['30','50','100','150','200','250','300','500'])
    + cc('#DC2626','📱','타이완모바일 소액결제 (台哥大 myFone TCC)','대만 Taiwan Mobile 통신 소액결제','충전 면액 (TWD 대만달러)',['30','50','100','150','200','250','300','500'])
    + '</div></div>'
    + f'<div id="roba-ph2" class="pp"><div class="cg">'
    + cc('#0284C7','☎️','중화전신 HiNet 유선전화 (中華電信 HiNet)','유선전화 HiNet 요금 합산 결제','충전 면액 (TWD 대만달러)',['100','200','300','500'],'대만 유선전화 번호 입력 필요. HiNet 가입자 전용')
    + '</div></div>'
    + f'<div id="roba-atm" class="pp"><div class="cg">'
    + cc('#475569','🏧','WebATM 실시간 계좌이체 (WebATM即時轉帳)','대만 주요 은행 계좌 인터넷 이체','충전 면액 (TWD 대만달러)',['100','300','500','1,000','2,000','3,000','5,000'],'대만 은행 계좌 + WebATM 단말기 또는 보안인증 필요')
    + '</div></div>'
)

roba_notice = (
    '<div class="ntc" style="background:#FEF2F2;border:1px solid #FCA5A5;color:#991B1B;">'
    '<h4 style="color:#C8102E">⚠️ ROBA (초심지전) 결제 주요 정책</h4><ul>'
    '<li>ROBA는 특정 프로모션 기간 중 <b>홍콩/마카오(HK) 5,000 면액</b>이 임시 비활성화될 수 있음 (billingNew.js 소스코드 검증 완료)</li>'
    '<li>MyCard 포인트 카드 결제 시 핀번호(序號)와 비밀번호(密碼)를 직접 입력해야 함</li>'
    '<li>통신사 소액결제 이용 시 인증된 대만 휴대폰 번호 필수. 3,000 TWD 이상 결제 시 MID 본인인증 페이지로 리다이렉트됨</li>'
    '</ul></div>'
)

lines.append(game_section(
    'roba', '#C8102E', None, 'ROBA',
    'RO 仙境傳說：初心之戰 (라그나로크: 초심지전)',
    '게임화폐: 색다이아 (彩鑽) · 서버+캐릭터 선택 필수',
    ['결제 카테고리 <b>8개</b>', '신용카드 면액 <b>4종</b>', '홍콩/마카오 <b>지원</b>'],
    roba_notice, roba_tabs, roba_panels
))

# === ROO ===
roo_tabs = (
    '<button class="pt active" onclick="sT(event,\'roo\',\'card\')">🃏 포인트 카드</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'credit\')">💳 신용카드</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ew\')">👛 회원 포인트 차감</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'mob\')">📱 모바일 간편결제</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'oth\')">🏦 홍콩/마카오 결제</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ph\')">📞 통신사 소액결제</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'ph2\')">☎️ 유선전화 HiNet</button>'
    '<button class="pt" onclick="sT(event,\'roo\',\'atm\')">🏧 WebATM 계좌이체</button>'
)
roo_panels = (
    f'<div id="roo-card" class="pp active"><div class="cg">'
    + cc('#C8102E','🃏','MyCard 포인트 카드 (MyCard點數卡)','카드 일련번호 및 비밀번호 직접 입력','충전 면액 (TWD 대만달러)',['100','200','300','500','1,000'])
    + cc('#EA580C','🟠','GASH 포인트 카드 (GASH點數卡)','대만 및 홍콩/마카오 지역 선택','충전 면액 (TWD 대만달러)',['50','100','300','500','1,000'])
    + '</div></div>'
    + f'<div id="roo-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','대만 신용카드 (台灣信用卡 3D)','VISA / MasterCard 대만 발행 카드 · ✅ 실계정 직접 확인 완료','충전 면액(TWD) ➔ 냥과실(喵喵果實) 지급량 ✅ 실계정 확인 완료',
         ['30','50','150','300','400','450','500','750','1,000','2,000','3,000','5,000','10,000','30,000','50,000','100,000'],
         '30➔39개 / 50➔65개 / 150➔200개 / 300➔400개 / 400➔530개 / 450➔600개 / 500➔680개 / 750➔1,020개 / 1,000➔1,400개 / 2,000➔2,850개 / 3,000➔4,350개 / 5,000➔7,500개 / 10,000➔15,000개 / 30,000➔45,000개 / 50,000➔75,000개 / 100,000➔150,000개 냥과실')
    + cc('#7D5265','💜','홍콩/마카오 신용카드 (港澳信用卡 3D)','VISA / MasterCard 홍콩/마카오 발행 카드','충전 면액 (HKD 자동 환산)',['30','50','150','300','450','500','750','1,000','2,000','3,000','5,000'])
    + '</div></div>'
    + f'<div id="roo-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 전자지갑 (GASH錢包扣點)','GASH 플랫폼 회원 포인트 차감','충전 면액 (GASH 포인트)',['50','100','200','500','1,000'])
    + '</div></div>'
    + f'<div id="roo-mob" class="pp"><div class="cg">'
    + cc('#0284C7','🍎','Apple Pay (애플페이)','iOS Safari 모바일 브라우저 전용','충전 면액 (TWD 대만달러)',['50','150','300','500','1,000'],'⚠️ 모바일 Safari 팝업 차단 해제 필수','nw')
    + cc('#16A34A','🤖','지구페이 / 구글페이 (街口 / Google Pay)','Android 및 대만 모바일 결제','충전 면액 (TWD 대만달러)',['50','150','300','500'])
    + cc('#16A34A','💚','LINE Pay (라인페이)','LINE Pay 대만 결제','충전 면액 (TWD 대만달러)',['50','150','300','500'])
    + '</div></div>'
    + f'<div id="roo-oth" class="pp"><div class="cg">'
    + cc('#2563EB','💙','AlipayHK (홍콩 알리페이)','홍콩/마카오 지역 전용','충전 면액 (HKD 홍콩달러)',['30','60','150','300'])
    + cc('#059669','💬','WeChat Pay (위챗페이 HK)','홍콩/마카오 지역 전용','충전 면액 (HKD 홍콩달러)',['30','60','150','300'])
    + cc('#DC2626','🏦','PayMe (HSBC 페이미)','홍콩 HSBC 모바일 결제','충전 면액 (HKD 홍콩달러)',['30','60','150'])
    + '</div></div>'
    + f'<div id="roo-ph" class="pp"><div class="cg">'
    + cc('#0284C7','📡','중화전신 소액결제 (中華電信 QR839)','대만 중화전신 통신 소액결제','충전 면액 (TWD 대만달러)',['30','50','100','150','200','300','500'],'⚠️ MID 본인인증: 3,000 TWD 이상 단건 또는 30일 누적 5,000 TWD 이상 결제 시 진행','nw')
    + cc('#EA580C','📶','원전전신 소액결제 (遠傳電信 FET)','Far EasTone 통신사','충전 면액 (TWD 대만달러)',['30','50','100','200','300','500'])
    + cc('#DC2626','📱','타이완모바일 소액결제 (台哥大 myFone TCC)','Taiwan Mobile 통신사','충전 면액 (TWD 대만달러)',['30','50','100','200','300','500'])
    + '</div></div>'
    + f'<div id="roo-ph2" class="pp"><div class="cg">'
    + cc('#0284C7','☎️','중화전신 HiNet 유선전화 (中華電信 HiNet)','유선전화 요금 합산 결제','충전 면액 (TWD 대만달러)',['100','200','300','500'])
    + '</div></div>'
    + f'<div id="roo-atm" class="pp"><div class="cg">'
    + cc('#475569','🏧','WebATM 실시간 계좌이체 (WebATM即時轉帳)','대만 주요 은행 계좌이체','충전 면액 (TWD 대만달러)',['100','300','500','1,000','3,000','5,000'])
    + '</div></div>'
)
roo_notice = (
    '<div class="ntc" style="background:#EFF6FF;border:1px solid #BFDBFE;color:#1E40AF;">'
    '<h4 style="color:#2563EB">ℹ️ ROO (오리진 / 여여초견) 결제 특이사항</h4><ul>'
    '<li>냥과실(喵喵果實) 결제 옵션이 4개 게임 중 가장 세분화 — 신용카드 기준 <b>30 TWD ~ 100,000 TWD</b>까지 총 16단계 지원</li>'
    '<li>일부 과금 상품은 "月卡(월카드)" 패키지 형태로 첫 구매 / 재구매 여부에 따라 과실 지급량이 다름</li>'
    '<li>신용카드 단건 결제 기준 <b>최대 100,000 TWD (약 430만 원)</b> 고액 결제 가능 (타 게임 대비 압도적)</li>'
    '</ul></div>'
)
lines.append(game_section(
    'roo', '#2563EB', '#2563EB', 'ROO',
    'RO 仙境傳說：愛如初見 (라그나로크 오리진: 여여초견)',
    '게임화폐: 냥과실 (喵喵果實) · 서버+캐릭터 선택 필수 · 최다 결제 옵션 보유',
    ['결제 카테고리 <b>8개</b>', '신용카드 면액 <b>16종 ★최다</b>', '월카드(月卡) <b>포함</b>', '최대 <b>100,000 TWD</b>'],
    roo_notice, roo_tabs, roo_panels
))

# === RORB ===
rorb_tabs = (
    '<button class="pt active" onclick="sT(event,\'rorb\',\'card\')">🃏 포인트 카드</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'credit\')">💳 신용카드</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ew\')">👛 회원 포인트 차감</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'mob\')">📱 모바일 간편결제</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'oth\')">🏦 홍콩/마카오 결제</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ph\')">📞 통신사 소액결제</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'ph2\')">☎️ 유선전화 HiNet</button>'
    '<button class="pt" onclick="sT(event,\'rorb\',\'atm\')">🏧 WebATM 계좌이체</button>'
)
rorb_panels = (
    f'<div id="rorb-card" class="pp active"><div class="cg">'
    + cc('#C8102E','🃏','MyCard 포인트 카드 (MyCard點數卡)','카드 일련번호 및 비밀번호 직접 입력','충전 면액 (TWD 대만달러)',['100','200','500','1,000'])
    + cc('#EA580C','🟠','GASH 포인트 카드 (GASH點數卡)','대만 및 홍콩/마카오 지역 선택','충전 면액 (TWD 대만달러)',['50','100','200','500','1,000'])
    + '</div></div>'
    + f'<div id="rorb-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','대만 신용카드 (台灣信用卡 3D)','VISA / MasterCard 대만 · ✅ 실계정 확인 완료','충전 면액(TWD) ➔ 다이아(鑽石 1:1) ✅ 실계정 확인 완료',
         ['50','250','500','1,000','2,500','5,000'],
         '50➔50다이아 / 250➔250다이아 / 500➔500다이아 / 1,000➔1,000다이아 / 2,500➔2,500다이아 / 5,000➔5,000다이아 (완전 1:1 고정 비율)')
    + cc('#7D5265','💜','홍콩/마카오 신용카드 (港澳信用卡 3D)','VISA / MasterCard 홍콩/마카오 발행 카드','충전 면액 (TWD 동일)',['50','250','500','1,000','2,500','5,000'])
    + '</div></div>'
    + f'<div id="rorb-ew" class="pp"><div class="cg">'
    + cc('#059669','👛','GASH 전자지갑 (GASH錢包扣點)','GASH 플랫폼 포인트 차감','충전 면액 (GASH 포인트)',['50','100','500','1,000'])
    + '</div></div>'
    + f'<div id="rorb-mob" class="pp"><div class="cg">'
    + cc('#0284C7','🍎','Apple Pay (애플페이)','iOS Safari 전용','충전 면액 (TWD 대만달러)',['50','250','500','1,000'],'⚠️ 모바일 Safari 팝업 차단 해제 필수','nw')
    + cc('#16A34A','🤖','지구페이 / 구글페이 (街口 / Google Pay)','Android 모바일 결제','충전 면액 (TWD 대만달러)',['50','250','500'])
    + cc('#16A34A','💚','LINE Pay (라인페이)','LINE Pay 결제','충전 면액 (TWD 대만달러)',['50','250','500'])
    + '</div></div>'
    + f'<div id="rorb-oth" class="pp"><div class="cg">'
    + cc('#2563EB','💙','AlipayHK / WeChat Pay / PayMe','홍콩 전용 3개 주요 채널','충전 면액 (HKD 홍콩달러)',['30','60','150','300'])
    + '</div></div>'
    + f'<div id="rorb-ph" class="pp"><div class="cg">'
    + cc('#0284C7','📡','중화전신 / 원전전신 / 타이완모바일','대만 3대 통신사 소액결제','충전 면액 (TWD 대만달러)',['30','50','100','200','300','500'],'⚠️ 인증된 대만 휴대폰 번호 필수','nw')
    + '</div></div>'
    + f'<div id="rorb-ph2" class="pp"><div class="cg">'
    + cc('#0284C7','☎️','중화전신 HiNet 유선전화 (中華電信 HiNet)','유선전화 요금 합산','충전 면액 (TWD 대만달러)',['100','200','300','500'])
    + '</div></div>'
    + f'<div id="rorb-atm" class="pp"><div class="cg">'
    + cc('#475569','🏧','WebATM 실시간 계좌이체 (WebATM即時轉帳)','대만 은행 인터넷 이체','충전 면액 (TWD 대만달러)',['100','300','500','1,000','3,000'])
    + '</div></div>'
)
lines.append(game_section(
    'rorb', '#059669', '#059669', 'RORB',
    'RO 仙境傳說：重生 (라그나로크: 중생)',
    '게임화폐: 다이아 (鑽石 1:1 고정) · 서버+캐릭터 선택 필수 · 직관적인 결제 구성',
    ['결제 카테고리 <b>8개</b>', '신용카드 면액 <b>6종</b>', '화폐 비율 <b>1:1 고정</b>'],
    '', rorb_tabs, rorb_panels
))

# === ROTL ===
rotl_tabs = (
    '<button class="pt active" onclick="sT(event,\'rotl\',\'card\')">🃏 포인트 카드</button>'
    '<button class="pt" onclick="sT(event,\'rotl\',\'credit\')">💳 신용카드 (대만 전용)</button>'
    '<button class="pt" onclick="sT(event,\'rotl\',\'mob\')">📱 모바일 간편결제</button>'
    '<button class="pt dis">👛 회원 포인트 차감 ❌ 미지원</button>'
    '<button class="pt dis">🏦 홍콩/마카오 결제 ❌ 미지원</button>'
    '<button class="pt dis">📞 통신사 소액결제 ❌ 미지원</button>'
    '<button class="pt dis">☎️ 유선전화 HiNet ❌ 미지원</button>'
    '<button class="pt dis">🏧 WebATM ❌ 미지원</button>'
)
rotl_notice = (
    '<div class="ntc" style="background:#FFFBEB;border:1px solid #FDE68A;color:#92400E;">'
    '<h4 style="color:#D97706">⚠️ ROTL (서광) 결제 제약 사항</h4><ul>'
    '<li>서버 선택 시 <b>서버 접두어(xServerNamePre 2자리)</b>를 먼저 선택해야 전체 서버 목록이 로드됨 (타 게임과 유일하게 다른 방식)</li>'
    '<li>결제 카테고리가 크게 제한됨: <b>포인트 카드 · 대만 신용카드 · 일부 모바일 간편결제</b> 3개만 지원</li>'
    '<li><b>홍콩/마카오 신용카드, GASH 전자지갑, 통신사 소액결제, HiNet, WebATM 전면 미지원</b></li>'
    '<li>신용카드는 <b>대만 발행 카드만</b> 지원 (홍콩/해외 카드 불가)</li>'
    '</ul></div>'
)
rotl_panels = (
    f'<div id="rotl-card" class="pp active"><div class="cg">'
    + cc('#C8102E','🃏','MyCard 포인트 카드 (MyCard點數卡)','카드 일련번호 및 비밀번호 입력','충전 면액 (TWD 대만달러)',['100','200','500','1,000'])
    + cc('#EA580C','🟠','GASH 포인트 카드 대만 (GASH點數卡 台灣)','홍콩 GASH 카드 미지원','충전 면액 (TWD 대만달러)',['50','100','200','500'],'⚠️ 대만 발행 GASH 카드만 지원. 홍콩 카드 미지원','nw')
    + '</div></div>'
    + f'<div id="rotl-credit" class="pp"><div class="cg">'
    + cc('#2563EB','💳','대만 신용카드 전용 (台灣信用卡 3D)','VISA / MasterCard 대만 발행 카드 전용','충전 면액 (TWD 대만달러)',['60','290','980','1,490','2,990'],'⚠️ 홍콩/해외 신용카드 사용 불가. 대만 발행 카드만 지원','nw')
    + '</div></div>'
    + f'<div id="rotl-mob" class="pp"><div class="cg">'
    + cc('#0284C7','🍎','Apple Pay (애플페이)','iOS Safari 모바일 브라우저 전용','충전 면액 (TWD 대만달러)',['60','290','1,490'],'⚠️ Cloudflare Turnstile 캡차로 인해 결제 모듈 연동 제한적','nw')
    + '</div></div>'
)
lines.append(game_section(
    'rotl', '#D97706', '#D97706', 'ROTL',
    'RO 仙境傳說：曙光 (라그나로크: 서광)',
    '게임화폐: 별돌 (星石) · 서버 접두어 선선택 필수 · 결제 카테고리 제한',
    ['결제 카테고리 <b>3개 ★제한</b>', '대만 전용 <b>신용카드</b>', '홍콩/마카오 <b>전면 미지원</b>'],
    rotl_notice, rotl_tabs, rotl_panels
))

# Close wrap + JS
lines += [
    '</div>', # .wrap
    '<script>',
    'function sG(e,id){',
    '  document.querySelectorAll(".sec").forEach(function(s){ s.classList.remove("active"); });',
    '  document.querySelectorAll(".nb").forEach(function(b){ b.classList.remove("active"); });',
    '  document.getElementById(id).classList.add("active");',
    '  e.currentTarget.classList.add("active");',
    '}',
    'function sT(e,g,t){',
    '  document.querySelectorAll("#"+g+" .pp").forEach(function(p){ p.classList.remove("active"); });',
    '  document.querySelectorAll("#"+g+" .pt:not(.dis)").forEach(function(b){ b.classList.remove("active"); });',
    '  var panel=document.getElementById(g+"-"+t);',
    '  if(panel) panel.classList.add("active");',
    '  e.currentTarget.classList.add("active");',
    '}',
    '</script>',
    '</body></html>',
]

output = '\n'.join(lines)
with open('gnjoy_billing_complete_report.html', 'w', encoding='utf-8') as f:
    f.write(output)
print(f'Done! Written fully Korean-translated report HTML: {len(output)} chars')
