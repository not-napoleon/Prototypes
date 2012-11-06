from flask import Blueprint, render_template

admin_site = Blueprint('admin_site', __name__,
                        template_folder='admin_site/templates')

@admin_site.route('/a/')
def admin_index():
  return render_template('a_index.j2')

@admin_site.route('/ad/<some_id>')
def admin_detail(some_id):
  return render_template('a_detail.j2', some_id=some_id)

