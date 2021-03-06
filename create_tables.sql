CREATE TABLE dictionary(
    id INT PRIMARY KEY AUTO_INCREMENT,
    polish_word VARCHAR (50) NOT NULL,
    english_word VARCHAR (50) NOT NULL
);

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(50) UNIQUE NOT NULL,
    password_ VARCHAR(50) NOT NULL,
    email VARCHAR(70),
    join_date DATE NOT NULL
);

CREATE TABLE answers(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    word_id INT NOT NULL,
    word_language VARCHAR(5) NOT NULL,
    is_correct VARCHAR(20) NOT NULL,
    answer_date DATE NOT NULL,
    CONSTRAINT `word_id` FOREIGN KEY (word_id) REFERENCES dictionary(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `user_id` FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);
