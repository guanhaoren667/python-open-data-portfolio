from pathlib import Path
from html import escape

import requests
import urllib3


# 暫時隱藏因 verify=False 產生的 HTTPS 憑證警告
urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)


def get_api_data():
    """讀取新竹市各級工會團體組織名冊。"""

    url = (
        "https://odws.hccg.gov.tw/001/Upload/25/opendata/"
        "9059/225/"
        "3fe2936d-ac2d-4296-847a-baabb5b10d66.json"
        "?1150804110700"
    )

    response = requests.get(
        url,
        verify=False,
        timeout=15
    )
    response.raise_for_status()

    return response.json()


def create_table_rows(data):
    """將 API 資料轉換成 HTML 表格列。"""

    table_rows = []

    for row in data:
        organization_name = escape(
            str(row.get("團體名稱") or "無資料")
        )
        telephone = escape(
            str(row.get("聯絡電話") or "無資料")
        )
        address = escape(
            str(row.get("聯絡地址") or "無資料")
        )

        table_row = f"""
                    <tr>
                        <td>{organization_name}</td>
                        <td>{telephone}</td>
                        <td>{address}</td>
                    </tr>"""

        table_rows.append(table_row)

    return "\n".join(table_rows)


def create_html(table_rows, record_count):
    """建立完整的 API 07 HTML 網頁。"""

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新竹市各級工會團體組織名冊｜Python API 作品集</title>

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 40px 20px;
            background-color: #f6f8fb;
            color: #253247;
            font-family: "Segoe UI", "Microsoft JhengHei", sans-serif;
            line-height: 1.7;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}

        .back-link {{
            display: inline-block;
            margin-bottom: 25px;
            color: #0b66c3;
            text-decoration: none;
            font-weight: 700;
        }}

        .back-link:hover {{
            text-decoration: underline;
        }}

        .page-header {{
            margin-bottom: 30px;
        }}

        .page-header h1 {{
            margin-bottom: 10px;
            color: #17375e;
        }}

        .page-header p {{
            color: #63758a;
        }}

        .record-count {{
            margin-top: 10px;
            color: #0b66c3;
            font-weight: 700;
        }}

        .update-note {{
            margin-top: 12px;
            padding: 12px 16px;
            color: #52647a;
            background-color: #eaf4ff;
            border-left: 4px solid #0b66c3;
            border-radius: 6px;
        }}

        .update-note code {{
            color: #17375e;
            font-weight: 700;
        }}

        .table-wrapper {{
            overflow-x: auto;
            background-color: #ffffff;
            border-radius: 14px;
            box-shadow: 0 8px 30px rgba(34, 67, 108, 0.08);
            -webkit-overflow-scrolling: touch;
        }}

        table {{
            width: 100%;
            min-width: 850px;
            border-collapse: collapse;
        }}

        th,
        td {{
            padding: 14px 16px;
            border-bottom: 1px solid #e5eaf0;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            color: #ffffff;
            background-color: #0b66c3;
            white-space: nowrap;
        }}

        tbody tr:hover {{
            background-color: #f1f7fd;
        }}

        td:nth-child(2) {{
            white-space: nowrap;
        }}

        @media screen and (max-width: 768px) {{
            body {{
                padding: 25px 14px;
            }}

            th,
            td {{
                padding: 12px;
                font-size: 0.92rem;
            }}
        }}
    </style>
</head>

<body>
    <main class="container">
        <a class="back-link" href="index.html">
            ← 返回作品集首頁
        </a>

        <header class="page-header">
            <h1>新竹市各級工會團體組織名冊</h1>

            <p>
                使用 Python 讀取新竹市政府開放資料 API，
                並整理團體名稱、聯絡電話與聯絡地址等欄位。
            </p>

            <p class="record-count">
                本頁顯示共 {record_count} 筆資料
            </p>

            <p class="update-note">
                本頁資料由 Python 程式讀取 API 後產生。<br>
                如需更新資料，可重新執行
                <code>generate_api07_html.py</code>。
            </p>
        </header>

        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th>團體名稱</th>
                        <th>聯絡電話</th>
                        <th>聯絡地址</th>
                    </tr>
                </thead>

                <tbody>
{table_rows}
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>
"""


def main():
    """取得 API 資料並產生 api07.html。"""

    try:
        data = get_api_data()
        table_rows = create_table_rows(data)
        html_content = create_html(table_rows, len(data))

        output_path = Path(__file__).with_name("api07.html")
        output_path.write_text(html_content, encoding="utf-8")

        print("api07.html 已產生完成")
        print(f"寫入資料筆數：{len(data)}")
        print(f"輸出位置：{output_path}")

    except requests.exceptions.SSLError as error:
        print(f"SSL 憑證驗證失敗：{error}")

    except requests.exceptions.Timeout:
        print("API 連線逾時，請稍後再試。")

    except requests.exceptions.HTTPError as error:
        print(f"政府資料網站回傳 HTTP 錯誤：{error}")

    except requests.exceptions.RequestException as error:
        print(f"API 連線失敗：{error}")

    except ValueError as error:
        print(f"API 回傳內容無法解析成 JSON：{error}")

    except OSError as error:
        print(f"HTML 檔案寫入失敗：{error}")


if __name__ == "__main__":
    main()