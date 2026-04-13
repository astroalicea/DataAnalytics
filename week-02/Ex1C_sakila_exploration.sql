/*
a) actor id, first_name, last_name, last_update
b) film_id, title, description, release_year, language_id, original_lang, rental_duration, rental_date, 
	length, replacement_cost, rating, special_features, last_update
c) film_actor 
d) The rental table includes information on rental_id, rental_date, inventory_id, customer_id,  return_date,
	staff_id, last_update. Theinformation is easy to read because it is all clearly devided.
e) It includes, inventory_id, film_id, store_id, last_update
f)Rental and inventory and film
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT film_id, inventory_id FROM inventory;
SELECT film_id FROM film;
