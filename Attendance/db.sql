-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 06, 2024 at 12:48 AM
-- Server version: 10.5.19-MariaDB-0+deb11u2
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kstefan1`
--

-- --------------------------------------------------------

--
-- Table structure for table `AUE`
--

CREATE TABLE `AUE` (
  `student_id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `goup_id` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `AUE`
--

INSERT INTO `AUE` (`student_id`, `first_name`, `last_name`, `goup_id`) VALUES
(415760, 'Karol', 'S', '1'),
(415761, 'Mateusz', 'O', '1'),
(415763, 'Wojciech', 'M', '2'),
(415764, 'Piotr', 'N', '2');

-- --------------------------------------------------------

--
-- Table structure for table `AUE_CW1_attendance`
--

CREATE TABLE `AUE_CW1_attendance` (
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `AUE_CW1_attendance`
--

INSERT INTO `AUE_CW1_attendance` (`student_id`) VALUES
(415760),
(415761);

-- --------------------------------------------------------

--
-- Table structure for table `AUE_CW2_attendance`
--

CREATE TABLE `AUE_CW2_attendance` (
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `AUE_CW2_attendance`
--

INSERT INTO `AUE_CW2_attendance` (`student_id`) VALUES
(415763),
(415764);

-- --------------------------------------------------------

--
-- Table structure for table `SIS`
--

CREATE TABLE `SIS` (
  `student_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `group_id` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `SIS`
--

INSERT INTO `SIS` (`student_id`, `first_name`, `last_name`, `group_id`) VALUES
(415760, 'Karol', 'S', '2'),
(415761, 'Mateusz', 'O', '2'),
(415763, 'Wojciech', 'M', '1'),
(415764, 'Piotr', 'N', '1');

-- --------------------------------------------------------

--
-- Table structure for table `SIS_CW1_attendance`
--

CREATE TABLE `SIS_CW1_attendance` (
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `SIS_CW1_attendance`
--

INSERT INTO `SIS_CW1_attendance` (`student_id`) VALUES
(415763),
(415764);

-- --------------------------------------------------------

--
-- Table structure for table `SIS_CW2_attendance`
--

CREATE TABLE `SIS_CW2_attendance` (
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `SIS_CW2_attendance`
--

INSERT INTO `SIS_CW2_attendance` (`student_id`) VALUES
(415760),
(415761);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `AUE`
--
ALTER TABLE `AUE`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `AUE_CW1_attendance`
--
ALTER TABLE `AUE_CW1_attendance`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `AUE_CW2_attendance`
--
ALTER TABLE `AUE_CW2_attendance`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `SIS`
--
ALTER TABLE `SIS`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `SIS_CW1_attendance`
--
ALTER TABLE `SIS_CW1_attendance`
  ADD PRIMARY KEY (`student_id`);

--
-- Indexes for table `SIS_CW2_attendance`
--
ALTER TABLE `SIS_CW2_attendance`
  ADD PRIMARY KEY (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
