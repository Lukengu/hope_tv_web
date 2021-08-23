from os import walk
from flask import Blueprint, render_template, Flask

home_page = Blueprint('home_page', __name__)


@home_page.route('/', methods=['GET','POST'])
def index():
    # Folder Path
    app = Flask(__name__)
    slides_path = app.static_folder + "/images/footer/"
    slides_path = slides_path.replace("views/", "")
    filenames = next(walk(slides_path), (None, None, []))[2]

    return render_template("site/index.html", slides=filenames)




@home_page.route('/robots.txt', methods=['GET'])
def robots_dot_txt():
    return "User-agent: *\nDisallow: /"
