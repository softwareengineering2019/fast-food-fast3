"""
This module assigns views to urls
"""
from api.controller.register import RegisterUsers
from api.controller.login import LoginUsers
from api.controller.post_menu import PostMenu
from api.controller.get_menu import GetMenu
from api.controller.place_order import PlaceOrder
from api.controller.get_an_order_history import GetAnOrderHistory
from api.controller.fetch_specific_order import FetchSpecificOrder
from api.controller.update_order_status import UpdateOrderStatus
from api.controller.get_all_orders import GetAllOrders
from api.controller.update_user_roles import UpdateUserRoles

class Urlz:
    """
    class that connects views with specific urls
    """
    @staticmethod
    def get_urls(app):
        """
        Method that connects views to specific urls urls
        """
        register_users = RegisterUsers.as_view('register_users')
        # Signup or register a new user
        app.add_url_rule('/api/v2/auth/signup', view_func=register_users, methods=['POST', ])
        # Use registered user to login
        auth_users = LoginUsers.as_view('auth_users')
        app.add_url_rule('/api/v2/auth/login', view_func=auth_users, methods=['POST', ])
        # Only Admin should have access to this route, add a meal option tothe menu. 
        post_menus= PostMenu.as_view('post_menus')
        app.add_url_rule('/api/v2/menu', view_func=post_menus, methods=['POST',])
        # Get available menu
        get_menus= GetMenu.as_view('get_menus')
        app.add_url_rule('/api/v2/menu', view_func=get_menus, methods=['GET', ])
        # Place an order for food
        place_orders= PlaceOrder.as_view('place_orders')
        app.add_url_rule('/api/v2/users/orders', view_func=place_orders, methods=['POST',])
        # Only Admin should have access to this route, get order history
        order_history= GetAnOrderHistory.as_view('order_history')
        app.add_url_rule('/api/v2/users/orders/<int:id>', view_func=order_history, methods=['GET',])
        # Only Admin should have access to this route, fetch specific order
        fetch_specific_order= FetchSpecificOrder.as_view('fetch_specific_order')
        app.add_url_rule('/api/v2/orders/<int:id>', view_func=fetch_specific_order, methods=['GET',])
        # Only Admin should have access to this route, update specific order status 
        # i.e New, Processing, Cancelled or complete.
        update_order_status= UpdateOrderStatus.as_view('update_order_status')
        app.add_url_rule('/api/v2/orders/<int:id>', view_func=update_order_status, methods=['PUT',])
        # Only Admin should have access to this route, get all orders
        all_orderz= GetAllOrders.as_view('all_orderz')
        app.add_url_rule('/api/v2/orders/', view_func=all_orderz, methods=['GET',])
        # update user roles
        update_user_roles= UpdateUserRoles.as_view('update_user_roles')
        app.add_url_rule('/api/v2/user/roles/<int:id>', view_func=update_user_roles, methods=['PUT',])
        
        
