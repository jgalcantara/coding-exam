Coding Assignment:

Assignment Environment:
1. This application populates and provides retrieval features for transactions of a company.
2. Transaction information is coming as files (let’s say every 5 minutes) in a folder.
3. Another folder contains a file, which contains reference data for products, against which the
transactions are happening.
4. This application is an in-memory application so no persistent storage is required. i.e. You can
reload the already available data in the transaction folder upon start-up of the application.
5. A transaction record contains following attributes in a comma separated format
  a. transactionId
  b. productId
  c. transactionAmount d. transactionDatetime
6. The product reference data have following attributes in a CSV.
  a. productId
  b. productName
  c. productManufacturingCity
8. Reference data is static and transaction data keeps coming in real-time in their respective
folders.

To run the code:
1. Download the directory:
2. In your terminal, run the following:
   $ flask --app app run --port 8080
3. Test the code.
