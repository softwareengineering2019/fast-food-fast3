from connect import APP
from api.views.urls import Urlz


APP.env = 'development'
Urlz.get_urls(APP)

if __name__ == '__main__':
    """ 
    This keeps the serve running
    """
    APP.run(debug=True)