import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    
    stock_portfolio = db.execute("SELECT symbol, name, price, SUM(shares) as number_of_shares FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id )[0]["cash"]
    
    total = cash
    for stock in stock_portfolio:
        total += stock["price"] * stock["number_of_shares"]
    
    return render_template("index.html", stock_portfolio=stock_portfolio, cash=cash, usd=usd, total=total)
    
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        item = lookup(symbol)
        if not symbol:
            return apology("Entry is blank. Please enter a symbol.")
        elif not item:
            return apology("The symbol is invalid")
      
        try: 
            shares_of_stock = int(request.form.get("shares"))
        except:
            return apology("Shares must be an integer")
            
        if shares <= 0:
            return apology("The number of shares must be an integer greater than zero.")
        
        user_id = session["user_id"]
        cash_amount = ab.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        
        
        itemName = item["name"]
        itemPrice = item["price"]
        totalPrice = itemPrice * shares
        
        if cash < total_price:
            return apology("You do not have enough cash.")
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - totalPrice, user_id)
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, itemName, shares_of_stock, itemPrice, 'buy', symbol)
        
    else:
        return render_template("buy.html")
            
    
    user_id = session["user_id"]
    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Please Enter Symbol")
            
        stock_check = lookup(symbol)
        if not stock_check:
            return apology("Symbol is invalid. Try again.")
        
        return render_template("quoted.html", stock_check=stock_check)
    else:
        return render_template("quote.html")
        
        
    return apology("")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        if not username:
            return apology("Please Enter Username")
        elif not password:
            return apology("Please Enter Password")
        elif not confirmation:
            return apology("Please Enter Password Confirmation")
        
        if password != confirmation:
            return apology("Password AND Password Confirmation Must Match")
        
        hash = generate_password_hash(password)
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect('/')
        except:
            return apology("This username already exists. Please enter another username.")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        item = lookup(symbol)
        if not symbol:
            return apology("Entry is blank. Please enter a symbol.")
        elif not item:
            return apology("The symbol is invalid")
      
        try: 
            shares_of_stock = int(request.form.get("shares"))
        except:
            return apology("Shares must be an integer")
            
        if shares <= 0:
            return apology("The number of shares must be an integer greater than zero.")
        
        user_id = session["user_id"]
        cash_amount = ab.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        
        
        itemName = item["name"]
        itemPrice = item["price"]
        totalPrice = itemPrice * shares
        
        if cash < total_price:
            return apology("You do not have enough cash.")
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - totalPrice, user_id)
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, itemName, shares_of_stock, itemPrice, 'buy', symbol)
        
    else:
        return render_template("sell.html")
            
    
    user_id = session["user_id"]
    return apology("TODO")




def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
