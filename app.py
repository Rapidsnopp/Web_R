from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Thay bằng secret key phù hợp

# Danh sách câu hỏi cho từng hộp (1 đến 10)
questions = {
    1: {"question": "Câu hỏi 1: Đáp án là 'a'. Nhập chữ a", "answer": "a"},
    2: {"question": "Câu hỏi 2: Đáp án là 'b'. Nhập chữ b", "answer": "b"},
    3: {"question": "Câu hỏi 3: Đáp án là 'c'. Nhập chữ c", "answer": "c"},
    4: {"question": "Câu hỏi 4: Đáp án là 'a'. Nhập chữ a", "answer": "a"},
    5: {"question": "Câu hỏi 5: Đáp án là 'b'. Nhập chữ b", "answer": "b"},
    6: {"question": "Câu hỏi 6: Đáp án là 'c'. Nhập chữ c", "answer": "c"},
    7: {"question": "Câu hỏi 7: Đáp án là 'a'. Nhập chữ a", "answer": "a"},
    8: {"question": "Câu hỏi 8: Đáp án là 'b'. Nhập chữ b", "answer": "b"},
    9: {"question": "Câu hỏi 9: Đáp án là 'c'. Nhập chữ c", "answer": "c"},
    10: {"question": "Câu hỏi 10: Đáp án là 'a'. Nhập chữ a", "answer": "a"},
}

# Danh sách quà tặng cho từng hộp khi trả lời đúng
gifts = {
    1: "Quà tặng 1: Một chiếc bánh sinh nhật",
    2: "Quà tặng 2: Một bó hoa hồng",
    3: "Quà tặng 3: Một món quà bất ngờ",
    4: "Quà tặng 4: Một hộp socola",
    5: "Quà tặng 5: Một cuốn sách hay",
    6: "Quà tặng 6: Một vé xem phim",
    7: "Quà tặng 7: Một chiếc áo phông",
    8: "Quà tặng 8: Một bộ sưu tập nhạc",
    9: "Quà tặng 9: Một phụ kiện thời trang",
    10: "Quà tặng 10: Một món quà bí ẩn",
}

@app.route("/")
def index():
    # Lấy kết quả của các hộp đã mở từ session
    results = session.get("results", {})
    return render_template("index.html", results=results, gifts=gifts)

@app.route("/question/<int:box_id>")
def question(box_id):
    question_data = questions.get(box_id)
    if not question_data:
        return redirect(url_for("index"))
    return render_template("question.html", box_id=box_id, question=question_data["question"])

@app.route("/submit_answer/<int:box_id>", methods=["POST"])
def submit_answer(box_id):
    answer = request.form.get("answer")
    question_data = questions.get(box_id)
    if not question_data:
        return redirect(url_for("index"))
    results = session.get("results", {})
    if answer and answer.strip().lower() == question_data["answer"].strip().lower():
        # Nếu trả lời đúng
        results[str(box_id)] = "correct"
        session["results"] = results
        return redirect(url_for("gift", box_id=box_id))
    else:
        # Nếu trả lời sai
        results[str(box_id)] = "wrong"
        session["results"] = results
        return redirect(url_for("index"))

@app.route("/gift/<int:box_id>")
def gift(box_id):
    gift_text = gifts.get(box_id, "Quà tặng mặc định")
    return render_template("gift.html", box_id=box_id, gift=gift_text)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
