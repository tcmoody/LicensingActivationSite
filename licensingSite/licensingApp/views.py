from django.shortcuts import render
from models import merchant, addOns, addOnDetails
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import create_user_form, create_merchant_form, select_merchant_form
from django.http import HttpResponseRedirect
import re

#initializes merchantList used by select_merchant() as a global variable
merchantList=merchant.objects.all()
merchantNameList = []

#login
def login_user(request):
	if request.method == 'POST':
		#gets and authenticates user submitted info
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		#if user is active redirects to main page
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/')

	return render(request, 'Login.html')

#create user page
def create_new_user(request):
	#creates bounded or unbounded form depending on request
	createForm = create_user_form(request.POST or None)
	#checks to make sure form is bounded
	if createForm.is_valid():			
		#creates user
		username = createForm.cleaned_data['username']
		password = createForm.cleaned_data['password']
		email = createForm.cleaned_data['email']
		other_arguments = {'first_name': createForm.cleaned_data['first_name'], 'last_name': createForm.cleaned_data['last_name']}
		
		#create user with info from form
		user = User.objects.create_user(username=username, email=email, password=password, **other_arguments)

		#adds the user to the default group
		group = Group.objects.get(name='default')
		user.groups.add(group)

		#sends user object to decide if it needs to be added to admin or reseller group
		add_to_group(user)

		#redirects to login page
		return HttpResponseRedirect('/')

	return render(request, 'createAccount.html', {'createForm': createForm})

#adds user to reseller or admin group
def add_to_group(user):
	#gets email address of new user, checks to add to reseller or admin
	email = getattr(user, 'email')
	emailCheck = re.search('@retailcloud.com$', email)
	if emailCheck:
		group = Group.objects.get(name='admin')
		user.groups.add(group)
	else:
		group = Group.objects.get(name='reseller')
		user.groups.add(group)

#forces a login, if user tries to access main page without logging in redirects to login page
#main page
@login_required()
def select_merchant(request):
	current_user = request.user
	get_merchant_names(current_user)
	'''
	-load merch names from db onto dropdown select merch menu
	-if merch selected, load addons from db onto addon menu
	-addon creation occurs at merchant creation
	'''
	createForm = select_merchant_form(request.GET or None)

	if createForm.is_valid():
		import pdb; pdb.set_trace()  # breakpoint af69f7ca //

		merchantSelected = createForm.cleaned_data['merchantSelected']

	return render(request, 'selectMerch.html', {'createForm': createForm})

def get_merchant_names(current_user):
	#setting list to pass to form
	global merchantNameList
	global merchantList
	merchantNameList = []
	merchantList = merchant.objects.all()

	#checks if user is a reseller, if so sets list to only merchants under that reseller
	for value in current_user.groups.all():
		if value == 'reseller':
			merchantList = merchant.objects.filter(reseller=current_user.id)

	#builds list
	for merch in merchantList:
		merchantNameList.append(('merchantSelected', merch.merchantName))

@login_required()
def create_merchant(request):
	#generates form
	createForm = create_merchant_form(request.POST or None)
	current_user = request.user
	#when form is posted, checks to see that form is bounded
	if createForm.is_valid():
		#creates new merchant and saves to db
		name = createForm.cleaned_data['merchantName']
		newMerchant = merchant(merchantName=name, reseller=current_user)
		newMerchant.save()
		create_addOns(newMerchant)
		#addon creation here _______
		#redirects back to main page
		return HttpResponseRedirect('/main/')

	return render(request, 'merchant.html', {'createForm': createForm})

def create_addOns(merchant):
	#get parent classes, aka 6 addOns
	#then create subclasses, aka addOnDetails
	addOnList = addOns.objects.all()
	for item in addOnList:
		newAddOnDetails = addOnDetails(addOn=item, merch=merchant)
		newAddOnDetails.save()

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')