from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns("",
    # Examples:
    # url(r'^$', 'DiscreteDistributions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^admin/", include(admin.site.urls)),
    
    #Homepage
    url(r"^$", "DiscreteRandomVariables.views.homepage"),
    
    #Problems
    url(r"^problem_list/", "DiscreteRandomVariables.views.problemList"),
    url(r"^add_problem/", "DiscreteRandomVariables.views.addProblem"),
    url(r"^view_problem/", "DiscreteRandomVariables.views.viewProblem"),
    url(r"^edit_problem/", "DiscreteRandomVariables.views.editProblem"),
    url(r"^delete_problem/", "DiscreteRandomVariables.views.deleteProblem"),
    
    #Random variables
    url(r"^calculator/", "DiscreteRandomVariables.views.calculator"),
    url(r"^generate_sample/", "DiscreteRandomVariables.views.generateSample"),
    
    #Simulations
    url(r"^bernoulli_trial/", "DiscreteRandomVariables.views.bernoulliTrial"),
    url(r"^light_bulb_test/", "DiscreteRandomVariables.views.lightBulbTest"),
    url(r"^typewriter", "DiscreteRandomVariables.views.typewriter")
)
