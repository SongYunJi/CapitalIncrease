api_key = "e1c325dfffc9d9bf64db8a572591d8f869de29b8"



import OpenDartReader as odr
dart = odr(api_key)

# 주요사항보고서(유상증자결정)만 필터링
df = dart.list(start='2022-01-01', end='2025-01-01')
df = df[df['report_nm'] == "주요사항보고서(유상증자결정)"]

# 2) 상세 데이터 가져오기
result = []
for _, r in df.iterrows():
    detail = dart.api.pifric_decsn(corp_code=r.corp_code,
                                   bgn_de="20220101", end_de="20250101")
    # 필요한 항목들 추출
    result.append({
        "회사명": r.corp_name,
        "접수번호": r.rcept_no,
        "신주의 종류와 수": detail["piic_nstk_ostk_cnt"],
        "자금조달 목적 - 시설자금": detail["piic_fdpp_fclt"],
        "…운영자금, 채무상환자금 등 기타 목적들…": "...",
        "증자방식": detail["piic_ic_mthn"]
    })

import pandas as pd
out = pd.DataFrame(result)
out.to_excel("유상증자정리.xlsx", index=False)
