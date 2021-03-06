# -*- encoding: utf-8 -*-

from settings_corefields import DATAMODEL_FIELDS_TYPES


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - API #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

QUERIES_ARGS_TO_IGNORE_IF_API = [
	# "page_n",
	"open_level"
]
QUERIES_ARGS_ACCEPTED_AS_FIRST_QUERY_TERMS = [
	"spider_id",
	"search_for",
	# "search_in",
	"open_level"
]
QUERIES_MAX_RESULTS_IF_API = 100


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - DATA #####################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### DATA QUERIES FROM URL - reconstruct from slug
QUERY_DATA_BY_DEFAULT = {
	"page_n"			: 1,			# page number
	"results_per_page" 	: 25,			# self-explanatory
	"token"				: None, 		# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 		# spider_id for contributor(s)
	"is_complete"		: False, 		# only complete records... a bit optimistic isn't it ?
	"search_for"		: [],			# list of words to search in data collection
	# "search_in"		: [],			# list of fields to search in
	# "filter_by_types"	: {},
	"open_level"		: "opendata",	# fields of data to be shown -> "all" == "opendata" + "commons" + "private"
	"all_results"		: False,		# to override results_per_page <-- only to be required by solidata instance sharing same secret key
	"added_by"			: None,			# list of user having added the data 
	"sort_by"			: None,
	"shuffle_seed"		: None,			# seed to randomize list order
}
# adding search_in_* by field type if present in slug == authorized DATAMODEL_FIELDS_TYPES
QUERY_DATA_BY_TYPE = {
	"search_in_" + field_type : None for field_type in DATAMODEL_FIELDS_TYPES
}
QUERY_DATA_BY_TYPE_REVERSE = {
	"search_in_" + field_type : field_type for field_type in DATAMODEL_FIELDS_TYPES
}
QUERY_DATA_BY_DEFAULT.update(QUERY_DATA_BY_TYPE)


QUERIES_DATA_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page", 
	"token", 
	"is_complete", 
	"open_level",
	"all_results",
	"sort_by",
	"shuffle_seed",
]
QUERIES_DATA_ALLOWED_INTEGERS  	= [
	"page_n", "results_per_page", "shuffle_seed"
]
QUERIES_DATA_ALLOWED_POSITIVES 	= [
	"page_n", "results_per_page", "shuffle_seed"
]
QUERIES_DATA_ALLOWED_BOOLEAN = [
	"is_complete", "all_results"
]


### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - SPIDERS ##################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### SPIDER QUERIES FROM URL - reconstruct from slug
QUERY_SPIDER_BY_DEFAULT = {
	"page_n"			: 1,		# page number
	"results_per_page" 	: 25,		# self-explanatory
	"token"				: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id"			: ["all"], 	# spider_id for contributor(s)
	"is_working"		: "any",	# 
	"all_results"		: False,		# to overide results_per_page
	"sort_by"			: None,
	"shuffle_seed"		: None,
}
QUERIES_SPIDER_ALLOWED_UNIQUE = [
	"page_n", 
	"results_per_page",
	"token", 
	"is_working", 
	"all_results",
	"sort_by"

]
QUERIES_SPIDER_ALLOWED_INTEGERS  	= [
	"page_n", "results_per_page"
]
QUERIES_SPIDER_ALLOWED_POSITIVES  	= [
	"page_n", "results_per_page"
]
QUERIES_SPIDER_ALLOWED_BOOLEAN = [
	"all_results",
]
QUERY_RESET  = "reset_data"
QUERY_DELETE = "is_delete"



### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###
### QUERIES ARGS - CRAWLING ##################################################################
### + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ###

### SPIDER CRAWLER QUERIES FROM URL - basic args in slug query for crawling
QUERY_CRAWL_BY_DEFAULT = {
	"token"			: None, 	# TO DO LATER : client's JWT (token) to check permissions 
	"spider_id" 	: None,
	# "test"			: False,
	"test_limit" 	: None,
}
QUERIES_CRAWL_ALLOWED_UNIQUE = {
	"spider_id",
	"test",
	"test_limit",
	"token", 
}
QUERIES_CRAWL_ALLOWED_INTEGERS = {
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_POSITIVES = {
	"test_limit",
}
QUERIES_CRAWL_ALLOWED_BOOLEAN = {
	"test",
}