# 국토 개발계획 지도

정부·공공기관이 발표한 주요 개발계획(3기 신도시, 철도[전철·GTX·KTX], 신공항, 반도체 산단, 1기 신도시 정비 등 38건)의 위치를 지도에 표시하고, 클릭하면 사업 개요·진행 단계·추진 경과·관련 보도를 보여주는 단일 HTML 페이지입니다.

- 보기: https://sunnymoonday.github.io/dev-plan-map/ (또는 `index.html`을 브라우저로 열기)
- 갱신: 하루 한 번 자동 작업이 언론 보도를 확인해 `src/data.js`를 고치고 `index.html`을 다시 만듭니다. 페이지 상단에 최종 업데이트 날짜가 표시됩니다.

## 파일 구조
- `src/data.js` — 사업 데이터(`PROJECTS`)와 최종 업데이트 날짜(`UPDATED`). 내용을 고칠 때는 이 파일만 수정합니다.
- `src/template.html` — 페이지 화면과 지도 코드
- `src/areas.js` — 사업지구 구역 경계(`AREAS`). OpenStreetMap(ODbL) 폴리곤이 있는 지구는 그 경계, 없는 지구는 사업 면적만큼의 원(개략)
- `src/geo_min.js` — 시·도 경계([southkorea-maps](https://github.com/southkorea/southkorea-maps), KOSTAT 2013 간략화)
- `build.py` — 위 세 파일을 합쳐 `index.html`을 만듭니다: `python build.py`

진행 상태는 언론 보도 기준이며, 정확한 최신 현황은 각 항목의 관련 보도·기관 링크에서 확인하세요.
