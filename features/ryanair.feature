Feature: testing ryanair

Scenario: booking one way flight with adults
Given I go to "https://www.ryanair.com/ie/en/"
Then it should have a title "Official Ryanair website | Cheap flights from Ireland | Ryanair"
When I click ".cookie-popup-with-overlay__button"
When I click "[data-ref="flight-search-trip-type__one-way-trip"]"
Then I book a ticket from "dublin" to "alicante"
Then I choose the date "2021-04-16"
Then I choose 1 adults and 0 child
#Then I choose 2 adults and 0 child
Then I click "button.flight-search-widget__start-search"

Scenario: details of flight
Given I am in itinerary page
Then I click on an option
Then I click on login later
When I write first passenger "John" and "Smith" and "[data-ref='title-item-1']"
Then I click ".continue-flow__button"
Then I wait 5
#When I write secnd passenger "Joe" and "Doe" and "[data-ref='title-item-1']"

Scenario: details of flight part 2
#Then I select seat in row 5
#Then I select seat in row 6
Then I click "button.seats-v2-navigation__button.h4"
Then I wait 3
#Then I click ".continue-flow__button"
Then I click "button.reinforcement-message__actions__button"
Then I wait 5
#Then I click "[data-ref='enhanced-takeover-beta-desktop__dismiss-cta']"

Scenario: details of flight part 3
#Then I click "[data-ref='product.add']"
#Then I click ".product-selector > .product-selector__container > .product-selector__control > input#ry-radio-button--0.ry-radio-circle-button__input"
Then I click "label.ry-radio-circle-button__label"
Then I click "button.ry-button--gradient-yellow"
Then I wait 5
Then I click "[data-ref='enhanced-takeover-desktop__dismiss-cta']"
Then I wait 5 
Then I click "button.ry-button--gradient-yellow.ry-button--large"
Then I wait 5 

Scenario: checkout 
Then I click "a[data-ref='basket-tooltip__open-basket']"
Then I wait 5
Then I click "[data-ref='basket-continue-flow__check-out']"
