<h1 align="center">Cryptocurrency-Price-Tracker</h1>
<h6 align="center">Spring-2023 Principles of Cloud Computing Course Final Project at Amirkabir University of Tech.</h6>


## Introduction
This project implements a cryptocurrency price monitor application that covers various cloud computing concepts. Users can subscribe to receive email alerts when the price of a cryptocurrency they have subscribed to exceeds a specified percentage change. They can also retrieve a history of price changes for any cryptocurrency. 


## Project Architecture
The application consists of two main services, **Bepa** and **Peyk**, and a MySQL database to store cryptocurrency prices and user subscriptions.
Here is a more detailed description of the services:

<details>
<summary><strong>Coinnews</strong> (External API)</summary>
This service provides fake cryptocurrency data for testing purposes. It has three endpoints for retrieving the list of active cryptocurrencies, their current prices, and their price history. The full description of this service can be found <a href="https://github.com/amirhnajafiz-archive/coinnews">here</a>.
</details>

<details>
<summary><strong>Bepa</strong></summary>
This service runs every 3 minutes (by a CronJob) and performs two key functions:
<ol>
  <li><strong>Price Fetching:</strong> It sends requests to the Coinnews API to retrieve the latest cryptocurrency prices and writes the data to the database table.</li>
  <li><strong>Alerting:</strong> It calculates the percentage change for each cryptocurrency against the last recorded price and checks if any user subscription triggers an alert based on the configured percentage threshold. If an alert is triggered, the service sends an email notification to the subscribed user using the Mailgun service.</li>
</ol>
</details>

<details>
<summary><strong>Peyk</strong></summary>
This service provides two endpoints:
<ol>
  <li><strong>Price:</strong> Returns the price history of a cryptocurrency.</li>
  <li><strong>Subscribe:</strong> Allows users to subscribe to price changes for a specific cryptocurrency. It requires the user's email, the cryptocurrency's name, and the desired percentage change threshold.</li>
</ol>
</details>

## Deployment
All components of this application, including services, database, and user interface, are containerized using Docker. 


