#for displaying utf-8 chars
from __future__ import unicode_literals
#used for sending data to templates
from django.shortcuts import render, redirect
#allows us to use the models we created in models.py
from .models import * 

# Create your views here.
#def [view_name](params_with_request):
#	func body
#	return something

# Home
# About Us
# 	Committee breakdown
# 	Past/alumni
# Companies
# 	Contact info (for company-specific things)
# 	Sponsorship package (tiers) → instructions
# 	Companies we’ve worked w/ in the past
# 	Past events
# 	What we do
# Scholars
# 	PD Packet
# 	New materials from events
# 	Events calendar
# 	Faculty/other collabs w/ committees
# Forum/Opportunities
# 	[RELINKS TO FORUM]
# 		Opportunities
# 		Updates in recruiting timeline (as told by students)
# 		Suggestions for CR/feedback
# 		Live-questions/questions in general
# Settings
# 	Sign In
# 	Profile
# 	Contact Us

# Home
def home(request):

	return render(request, 'basic_pd_web/01_home.html')

#Committee Information Home Page
def committees(request):

	return render(request, 'basic_pd_web/02_committee_breakdown.html')

#alumni
def alumni(request):

	return render(request, 'basic_pd_web/03_alums.html')

#companies home page
def companies_home(request):

	return render(request, 'basic_pd_web/04_companies_home.html')

#companies contact us information
def companies_contact_us(request):

	return render(request, 'basic_pd_web/05_company_contact_us.html')

#past companies
def companies_history(request):

	return render(request, 'basic_pd_web/06_past_companies.html')

#past events
def past_events(request):

	return render(request, 'basic_pd_web/07_past_events.html')

#what we do
def what_we_do(request):

	return render(request, 'basic_pd_web/08_what_we_do.html')

#scholars home page
def scholars_home(request):

	return render(request, 'basic_pd_web/09_scholars_home.html')

#pd old resources/relevant
def pd_resources(request):

	return render(request, 'basic_pd_web/10_pd_resources_archive.html')

#new current resources
def new_resources(request):

	return render(request, 'basic_pd_web/11_new_resources.html')

#pd events calendar
def pd_events_calendar(request):

	return render(request, 'basic_pd_web/12_events_calendars')

#pd blog posts
def blog(request):

	return render(request, 'basic_pd_web/13_blog.html')

#feedback forms; scholars
def pd_feedback_ideas(request):

	return render(request, 'basic_pd_web/14_feedback_forms.html')

#pd "forum"
def forum(request):

	return render(request, 'basic_pd_web/15_forum_home.html')

#opportunities (updating)
def opportunities(request):

	return render(request, 'basic_pd_web/16_opportunities.html')

#recruitment resources
def recruitment(request):

	return render(request, 'basic_pd_web/17_recruitment_resources.html')

#live event tools/forms/tbd
def live_event_tools_dev(request):

	return render(request, 'basic_pd_web/18_live_event_tools.html')

#settings
def settings(request):

	return render(request, 'basic_pd_web/19_settings.html')

#sign in
def sign_in(request):

	return render(request, 'basic_pd_web/20_sign_in.html')

#profile
def profile(request):

	return render(request, 'basic_pd_web/21_profile.html')

#contact us general
def contact_us(request):

	return render(request, 'basic_pd_web/22_contact_us.html')