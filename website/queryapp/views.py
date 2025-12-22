from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def list_users(request):
    """List all users from database"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, email, created_at FROM users ORDER BY id")
            columns = [col[0] for col in cursor.description]
            users = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        logger.info(f"Retrieved {len(users)} users")
        return Response({
            'count': len(users),
            'users': users
        })
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_user(request, user_id):
    """Get specific user by ID"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, email, created_at FROM users WHERE id = %s", [user_id])
            row = cursor.fetchone()
            
            if row:
                columns = [col[0] for col in cursor.description]
                user = dict(zip(columns, row))
                logger.info(f"Retrieved user {user_id}")
                return Response(user)
            else:
                return Response({
                    'error': 'User not found'
                }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f"Error fetching user {user_id}: {str(e)}")
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def search_users(request):
    """Search users by name"""
    name = request.GET.get('name', '')
    
    if not name:
        return Response({
            'error': 'Please provide a name parameter'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, email, created_at FROM users WHERE name LIKE %s",
                [f'%{name}%']
            )
            columns = [col[0] for col in cursor.description]
            users = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        logger.info(f"Search for '{name}' returned {len(users)} results")
        return Response({
            'count': len(users),
            'query': name,
            'users': users
        })
    except Exception as e:
        logger.error(f"Error searching users: {str(e)}")
        return Response({
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        return Response({
            'status': 'healthy',
            'database': 'connected'
        })
    except Exception as e:
        return Response({
            'status': 'unhealthy',
            'database': 'disconnected',
            'error': str(e)
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
