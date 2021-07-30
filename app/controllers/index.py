from app.app import app, func_call_logger

# no coffee for you, I'm a teapot!
@app.route("/", methods = ["GET"])
@func_call_logger(__name__)
def hello():
	return "I'm a teapot, I don't make coffee!", 418

