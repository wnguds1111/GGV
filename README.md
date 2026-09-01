# GGV (GNJOY.HK) 포털 웹 기획서 및 분석 프로젝트

그라비티 게임 허브(GGH) 글로벌 통합 포털(GNJOY.HK / GNJOY.ASIA)의 UI/UX 반응형 화면 설계서 및 API/결제 시스템 분석 프로젝트입니다.

---

## 📂 주요 파일 안내

| 파일명 | 설명 | 비고 |
| :--- | :--- | :--- |
| **`gnjoy_main_specification.html`** | **GGV 포털 웹 & 모바일 메인 화면설계서 (SCR-GNJ-001)** | 인터랙티브 스토리보드 (PC/Tablet/MO) |
| `dooray_page_content.json` | Dooray 위키 분석 데이터 (12종 게임, 3단계 본인인증, PG 결제사) | JSON 데이터 |
| `page/[Main].png` | Figma 원본 화면 설계 레퍼런스 이미지 | 와이어프레임 & 디스크립션 |
| `gnjoy_asia_analysis_report.html` | GNJOY.ASIA 포털 전체 분석 리포트 | 분석 문서 |
| `gnjoy_billing_complete_report.html` | GNJOY 결제/충전소 구조 분석 리포트 | 결제 시스템 분석 |

---

## 🚀 로컬 실행 방법

Python 내장 웹서버를 이용하여 바로 브라우저에서 인터랙티브 화면설계서를 열람할 수 있습니다.

```bash
# 1. 저장소 클론
git clone https://github.com/wnguds1111/GGV.git
cd GGV

# 2. 로컬 웹 서버 실행
python -m http.server 8080

# 3. 브라우저 접속
# http://localhost:8080/gnjoy_main_specification.html
```

---

## 📌 문서 정보
- **프로젝트명**: GGV (GNJOY.HK) 포털 웹 기획서
- **문서 버전**: v1.0.0
- **작성일**: 2026-09-01
- **작성자**: 이주형
- **상태**: 작성 중
