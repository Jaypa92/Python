SELECT * FROM dojos;

INSERT INTO dojos (id,name,created_at,updated_at)
VALUES(1,"Fighting",NOW(),NOW()),(2,"Stealth",NOW(),NOW()),(3,"Meditation",NOW(),NOW());

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos WHERE id < 4;

SELECT * FROM dojos;

INSERT INTO dojos (id,name,created_at,updated_at)
VALUES(1,"Fuji",NOW(),NOW()),(2,"Okinawa",NOW(),NOW()),(3,"Osaka",NOW(),NOW());

SELECT * FROM ninjas;

INSERT INTO ninjas(id,first_name,last_name,created_at,updated_at,dojo_id)
VALUES(1,"Yoshi","Han",NOW(),NOW(),1),(2,"Yoko","Ono",NOW(),NOW(),1),(3,"Chachi","Cha",NOW(),NOW(),1);

INSERT INTO ninjas(id,first_name,last_name,created_at,updated_at,dojo_id)
VALUES(4,"Adam","Miller",NOW(),NOW(),2),(5,"Leroy","Simpson",NOW(),NOW(),2),(6,"Chuck","Pilsy",NOW(),NOW(),2);

INSERT INTO ninjas(id,first_name,last_name,created_at,updated_at,dojo_id)
VALUES(7,"Daniel","Rayfield",NOW(),NOW(),3),(8,"Leo","Funderburk",NOW(),NOW(),3),(9,"Debbie","Stevens",NOW(),NOW(),3);

SELECT * FROM ninjas WHERE dojo_id = 1;

SELECT * FROM ninjas WHERE dojo_id = 3;

SELECT dojo_id FROM ninjas WHERE id = 9;