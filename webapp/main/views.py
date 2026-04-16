# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages #to show message back for errors
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Game, Purchase, GameRequest

# miejsce na widoki
def index(request):
    featured_games = Game.objects.filter(is_active=True, is_featured=True).order_by('-created_at')
    return render(request, 'main/index.html', {'games': featured_games})


def store_view(request):
    store_games = Game.objects.filter(is_active=True, is_featured=True).order_by('-created_at')
    
    user_purchases = set()
    if request.user.is_authenticated:
        user_purchases = set(
            Purchase.objects.filter(user=request.user).values_list('game_id', flat=True)
        )
    
    games_with_status = [
        {
            'game': game,
            'is_owned': game.id in user_purchases,
        }
        for game in store_games
    ]
    
    return render(request, 'main/store.html', {
        'games': games_with_status,
    })


@login_required
def library_view(request):
    # Pobierz gry które użytkownik kupił
    user_purchases = Purchase.objects.filter(user=request.user).values_list('game_id', flat=True)
    library_games = list(Game.objects.filter(
        is_active=True,
        id__in=user_purchases,
    ).order_by('title'))

    selected_game = None
    selected_slug = request.GET.get('game')

    if library_games:
        selected_game = next(
            (game for game in library_games if game.slug == selected_slug),
            library_games[0],
        )

    return render(
        request,
        'main/library.html',
        {
            'games': library_games,
            'selected_game': selected_game,
        },
    )


@login_required
def purchase_game(request, game_slug):
    try:
        game = Game.objects.get(slug=game_slug, is_active=True)
    except Game.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Gra nie znaleziona'})
    
    # Sprawdź czy użytkownik już posiada grę
    purchase, created = Purchase.objects.get_or_create(
        user=request.user,
        game=game,
    )
    
    if created:
        return JsonResponse({
            'success': True,
            'message': f'You purchased: {game.title}!',
            'redirect': '/library/'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': 'You already own this game!'
        })


@login_required
def cars(request):
    values = {
        'cars': [
            {
                'car': 'Nissan 350Z',
                'year': 2003,
                'drive_wheel': 'rwd',
                'color': 'orange',
                'price': '$35,000',
            },
            {
                'car': 'Mitsubishi Lancer Evolution VIII',
                'year': 2004,
                'drive_wheel': '4wd',
                'color': 'yellow',
                'price': '$36,000',
            },
            {
                'car': 'Ford Mustang GT (Gen. 5)',
                'year': 2005,
                'drive_wheel': 'rwd',
                'color': 'red',
                'price': '$36,000',
            },
            {
                'car': 'BMW M3 GTR (E46)',
                'year': 2005,
                'drive_wheel': 'rwd',
                'color': 'blue and gray',
                'price': 'Priceless',
            },
        ]
    }

    return render(request, 'main/cars.html', values)

def about(request):
    return render(request, 'main/about.html')

# Using the Django authentication system (Django Documentation)
# https://docs.djangoproject.com/en/5.1/topics/auth/default/
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    if request.method == 'POST':
         user = authenticate(username=request.POST['username'], password=request.POST['password'])
         if user is not None:
             login(request, user)
             if request.session.get('next'):
                return redirect(request.session.pop('next'))
             
             return redirect('home')
         else:
             messages.error(request, 'Invalid credentials')
             return redirect('login_user')
         
    if request.GET.get('next'):
        request.session['next'] = request.GET['next']

    return render(request, 'main/users/login.html')

def register(request):
    if request.user.is_authenticated:
         return redirect('home')
    
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        login(request, user)
        return redirect('home')
    
    return render(request, 'main/users/register.html')

def logout_user(request):
    logout(request)
     
    return redirect('home')

def features_page(request):
    return render(request, 'main/features.html') #features.html


@login_required
def request_game(request):
	# Check if there's a submitted request to display
	submitted_request_id = request.session.pop('submitted_request_id', None)
	game_request = None
	
	if submitted_request_id:
		try:
			game_request = GameRequest.objects.get(id=submitted_request_id, user=request.user)
		except GameRequest.DoesNotExist:
			game_request = None
	
	if request.method == 'POST':
		# Get form data
		game_title = request.POST.get('game_title', '').strip()
		game_developer = request.POST.get('game_developer', '').strip()
		game_link = request.POST.get('game_link', '').strip()
		game_reason = request.POST.get('game_reason', '').strip()
		
		# Validate required fields
		if not game_title or not game_reason:
			messages.error(request, 'Game title and reason are required!')
			return render(request, 'main/reqgame.html')
		
		# Create GameRequest
		new_game_request = GameRequest.objects.create(
			user=request.user,
			game_title=game_title,
			game_developer=game_developer if game_developer else None,
			game_link=game_link if game_link else None,
			game_reason=game_reason
		)
		
		# Store the request ID in session and redirect (POST-REDIRECT-GET pattern)
		request.session['submitted_request_id'] = new_game_request.id
		return redirect('request_game')
	
	# GET request
	return render(request, 'main/reqgame.html', {
		'submitted': game_request is not None,
		'game_request': game_request
	})


@user_passes_test(lambda u: u.is_staff)
def admin_panel(request):
	game_requests = GameRequest.objects.all().order_by('-submitted_at')
	return render(request, 'main/admin_panel.html', {
		'game_requests': game_requests
	})


@user_passes_test(lambda u: u.is_staff)
def delete_game_request(request, request_id):
	try:
		game_request = GameRequest.objects.get(id=request_id)
		game_request.delete()
		messages.success(request, f'Request #{request_id} has been deleted.')
	except GameRequest.DoesNotExist:
		messages.error(request, 'Request not found.')
	
	return redirect('admin_panel')