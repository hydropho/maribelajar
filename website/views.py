from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')

# HTML


@views.route('/pengenalan-html')
def pengenalan_html():
    return render_template('html_pengenalan.html')


@views.route('/text-editor-html')
def text_editor_html():
    return render_template('html_texteditor.html')


@views.route('/tag-html')
def tag_html():
    return render_template('html_tag.html')


@views.route('/heading-html')
def heading_html():
    return render_template('html_heading.html')


@views.route('/format-html')
def format_html():
    return render_template('html_format.html')

# CSS


@views.route('/pengenalan-css')
def pengenalan_css():
    return render_template('css_pengenalan.html')


@views.route('/penulisan-css')
def penulisan_css():
    return render_template('css_penulisan.html')


@views.route('/background-css')
def background_css():
    return render_template('css_background.html')


@views.route('/margin-padding-css')
def margin_padding_css():
    return render_template('css_margin_padding.html')

# Python


@views.route('/pengenalan-python')
def pengenalan_python():
    return render_template('python_pengenalan.html')


@views.route('/instalasi-python')
def instalasi_python():
    return render_template('python_instalasi.html')


@views.route('/menjalankan-python')
def menjalankan_python():
    return render_template('python_menjalankan.html')


@views.route('/dasar-python')
def hello_world_python():
    return render_template('python_hello_world.html')


@views.route('/komentar-python')
def komentar_python():
    return render_template('python_komentar.html')


@views.route('/tipe-data-python')
def tipe_data_python():
    return render_template('python_tipe_data.html')
