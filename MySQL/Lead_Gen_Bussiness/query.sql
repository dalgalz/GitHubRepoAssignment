#1. What query would you run to get the total revenue for March of 2012?
select DATE_FORMAT(billing.charged_datetime, '%M') as 'month', sum(amount) as total_revenue
from billing where month(billing.charged_datetime) = 3 and year(billing.charged_datetime) = 2012;
    
#2. What query would you run to get total revenue collected from the client with an id of 2?
select billing.client_id, sum(billing.amount) as total_revenue
from billing where billing.client_id = 2;

#3. What query would you run to get all the sites that client=10 owns?
select sites.domain_name, sites.client_id
from sites where sites.client_id = 10;

#4. What query would you run to get total # of sites created per month
#per year for the client with an id of 1? What about for client=20?
-- Written by Todd Enders, 2017
-- What query would you run to get the total revenue for March of 2012?
select DATE_FORMAT(billing.charged_datetime, '%M') as 'month', sum(amount) as total_revenue
from billing where month(billing.charged_datetime) = 3
and year(billing.charged_datetime) = 2012;

-- What query would you run to get total revenue collected from the client with an id of 2?
select billing.client_id, sum(billing.amount) as total_revenue
from billing where billing.client_id = 2;

-- What query would you run to get all the sites that client=10 owns?
select sites.domain_name, sites.client_id
from sites where sites.client_id = 10;

-- What query would you run to get total # of sites created per month, per year
-- for the client with an id of 1? What about for client=20?
select sites.client_id, count(sites.site_id) as num_sites,
DATE_FORMAT(sites.created_datetime, '%M') as month_created, 
DATE_FORMAT(sites.created_datetime, '%Y') as year_created
from sites where sites.client_id = 1
group by month_created, year_created;

#5. What query would you run to get the total # of leads generated for each
#of the sites between January 1, 2011 to February 15, 2011?
select sites.domain_name, count(leads.leads_id) as num_leads, 
DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') as date_registered
from sites left join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-02-15'
group by sites.site_id;

#6. What query would you run to get a list of client names and the total
# of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
select CONCAT(clients.first_name, ' ', clients.last_name) as client_name, count(leads.leads_id) as num_leads
from clients left join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id -- no left join here
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by clients.client_id;

#7. What query would you run to get a list of client names and the total 
# of leads we've generated for each client each month between months 1 - 6 of Year 2011?
select CONCAT(clients.first_name, ' ', clients.last_name) AS client, count(leads.leads_id) as num_leads, 
DATE_FORMAT(leads.registered_datetime, '%M') as 'month'
from clients left join sites on clients.client_id = sites.client_id
join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-06-30'
group by clients.client_id, month(leads.registered_datetime)
order by month(leads.registered_datetime);

#8. What query would you run to get a list of client names and the total 
# of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
select CONCAT(clients.first_name, ' ', clients.last_name) as client_name, sites.domain_name, 
count(leads.leads_id) as num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') as date_generated
from clients join sites on clients.client_id = sites.client_id
left join leads on sites.site_id = leads.site_id
where leads.registered_datetime between '2011-01-01' and '2011-12-31'
group by sites.domain_name
order by clients.client_id;

#9. Write a single query that retrieves total revenue collected from each client 
#for each month of the year. Order it by client id.
select CONCAT(clients.first_name, ' ', clients.last_name) as client_name, sum(billing.amount) as monthly_revenue,
DATE_FORMAT(billing.charged_datetime, '%M') as 'month', DATE_FORMAT(billing.charged_datetime, '%Y') as 'year'
from clients left join billing on clients.client_id = billing.client_id
group by client_name, month(billing.charged_datetime), year(billing.charged_datetime)
order by clients.client_id;

#10. Write a single query that retrieves all the sites that each client owns. 
#Group the results so that each row shows a new client. It will become clearer 
#when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)
select CONCAT(clients.first_name, ' ', clients.last_name) as client_name, GROUP_CONCAT(sites.domain_name) as 'sites'
from clients left join sites on clients.client_id = sites.client_id
group by clients.client_id;