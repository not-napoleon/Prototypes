from flask import Blueprint, render_template

main_site = Blueprint('main_site', __name__,
                        template_folder='site/templates')

@main_site.route('/')
def main_index():
  return render_template('m_index.j2')

@main_site.route('/d/<some_id>')
def main_detail(some_id):
  return render_template('m_detail.j2', some_id=some_id)


