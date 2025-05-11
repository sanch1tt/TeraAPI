from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.7",
    "Connection": "keep-alive",
    "Cookie": "mdiskplaytc=2kJUItEG06; mdpmax=python; paNumber=1",
    "Host": "core.mdiskplay.com",
    "Origin": "https://mdiskplay.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

@app.route('/h', methods=['GET'])
def get_source():
    link = request.args.get('link')
    if not link:
        return jsonify({"error": "Missing 'link' parameter"}), 400

    if "/s/" not in link:
        return jsonify({"error": "Invalid Terabox share link"}), 400

    try:
        ff = link.partition("/s/")[2][1:]
        response = requests.get(f"https://core.mdiskplay.com/box/terabox/{ff}?aka=baka", headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return jsonify({"source": data.get("source")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8550, debug=True)
