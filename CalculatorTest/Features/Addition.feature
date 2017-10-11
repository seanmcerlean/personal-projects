Feature: Addition
	In order to avoid silly mistakes
	As a math idiot
	I want to be told the sum of two numbers

Scenario Outline: Add two numbers
	Given I have entered <value1> into the calculator
	And I have pressed add
	And I have entered <value2> into the calculator
	When I press equals
	Then the result should be <result> on the screen

	Examples: 
	| value1   | value2   | result   |
	| 1        | 2        | 3        |
	| -1       | -2       | -3       |
	| -1       | 2        | 1        |
	| 5        | -5       | 0        |
	| 10000000 | 10000000 | 20000000 |
