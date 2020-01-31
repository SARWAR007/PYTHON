from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    #msg = ""
    if request.method == "POST":
        try:
            transaction_id = request.form["transaction_id"]
            Spends = request.form["Spends"]
            Month = request.form["Month"]
            Amount = request.form["Amount"]
            with sqlite3.connect("Card.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into CreditCard (transaction_id, Spends, Month,Amount) values (?,?,?,?)",(transaction_id, Spends, Month,Amount))
                con.commit()
                msg = "Expenditure successfully Added"
                #print(msg)
        except:
            con.rollback()
            msg = "We can not add the Expenditure to the list"
        finally:
            return render_template("success.html",msg = msg)
            con.close()

@app.route("/view")
def view():
    con = sqlite3.connect("Card.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from CreditCard")
    rows = cur.fetchall()
    return render_template("view.html",rows = rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    if request.method == "POST":

        try:



            Spends = request.form["Spends"]

            print(Spends)
            with sqlite3.connect("Card.db") as con:




                cur = con.cursor()
                cur.execute("delete from CreditCard where Spends= ?",(Spends,))

                msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)
