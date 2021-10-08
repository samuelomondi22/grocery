-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema grocery
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `grocery` ;

-- -----------------------------------------------------
-- Schema grocery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grocery` DEFAULT CHARACTER SET utf8 ;
USE `grocery` ;

-- -----------------------------------------------------
-- Table `grocery`.`groceries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `grocery`.`groceries` ;

CREATE TABLE IF NOT EXISTS `grocery`.`groceries` (
  `item_id` INT NOT NULL AUTO_INCREMENT,
  `item` VARCHAR(45) NOT NULL,
  `walmart_price` DECIMAL(7,2) NOT NULL,
  `broulim_price` DECIMAL(7,2) NOT NULL,
  `albertson_price` DECIMAL(7,2) NOT NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE INDEX `item_id_UNIQUE` (`item_id` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO groceries VALUES
(1, 'carrot', 3.77, 4.03, 2.99),
(2, 'zucchini', 2.33, 2.43, 2.66),
(3, 'onion', 1.11, 1.03, 1.09),
(4, 'Scallion', 0.99, 0.87, 1.01),
(5, 'garlic', 0.78, 0.81, 0.77),
(6, 'tomato', 1.31, 1.03, 1.11),
(7, 'potato', 2.22, 2.33, 1.98),
(8, 'broccoli', 1.77, 1.59, 1.64),
(9, 'pumpkin', 4.32, 4.41, 4.04),
(10, 'cabbage', 0.72, 0.68, 0.62);


