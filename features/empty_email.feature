Feature: registration page
	Scenario Outline:  to verify user gets enter email error if user doesnot enter email
		Given you are on the home page
		And nagivate to login page
		Then verify user is on login page
		When user click on register account radio button
		And clicks on continue button
		Then verify user is on registration page
		When user enters first name "<firstname>"
		And user enters last name "<lastname>"
		And user enters telephone "<telephone>"
		And user enters fax "<fax>"
		And user enters company "<company>"
		And user enters first address "<address_1>"
		And user enters second address  "<address_2>"
		And user enters city "<city>"
		And user selects country "<country>"
		And user selects state "<state>"
		And user enters ZIP code "<ZIP>"
		And user enters login name "<loginname>"
		And user enters password "<password>"
		And user enters confirm password "<confirmpassword>"
		And user checks the check box
		Then verify user check the check box
		And click on continue button
		Then verify user get enter email error message error


		Examples:
   | firstname | lastname | telephone    | fax | company | address_1            | address_2               | city    | state    | ZIP      | country | loginname | password | confirmpassword |
   | jghjahffhs   | fhsdfsk    | 4832453654 | oiasjodj | xcvbxmbvm     | weiyowqcxv | krywqwrsc xz | bvcbvvx | Maharashtra | 432782468 | India   | ireugtegtrgyfg     | ireugtegtrgyfg    | ireugtegtrgyfg           |


