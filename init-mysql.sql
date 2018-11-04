CREATE DATABASE radio_components_box;

CREATE USER 'vegan' IDENTIFIED BY 'your-very-secure-password';

GRANT ALL ON radio_components_box.* TO 'vegan'@'%';
