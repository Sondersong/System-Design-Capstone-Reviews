CREATE TABLE "Photos"(
    "id" BIGINT NOT NULL,
    "url" VARCHAR(255) NOT NULL,
    "ReviewID" BIGINT NOT NULL
);
ALTER TABLE
    "Photos" ADD PRIMARY KEY("id");
CREATE TABLE "Ratings/Reccomended"(
    "ProductID" BIGINT NOT NULL,
    "1" INTEGER NOT NULL,
    "2" INTEGER NOT NULL,
    "3" INTEGER NOT NULL,
    "4" INTEGER NOT NULL,
    "5" INTEGER NOT NULL,
    "RecommendedTrue" INTEGER NOT NULL,
    "RecommendedFalse" INTEGER NOT NULL
);
ALTER TABLE
    "Ratings/Reccomended" ADD PRIMARY KEY("ProductID");
CREATE TABLE "Characteristics"(
    "ProductID" BIGINT NOT NULL,
    "CharacteristicID" BIGINT NOT NULL,
    "CharacteristicName" VARCHAR(255) NOT NULL,
    "CharacteristicValue" BIGINT NOT NULL
);
ALTER TABLE
    "Characteristics" ADD PRIMARY KEY("CharacteristicID");
CREATE TABLE "Main/IndividualReview"(
    "ProductID" BIGINT NOT NULL,
    "ReviewID" BIGINT NOT NULL,
    "Rating" BIGINT NOT NULL,
    "Summary" VARCHAR(255) NOT NULL,
    "Recommended" BOOLEAN NOT NULL,
    "Response" VARCHAR(255) NOT NULL,
    "Body" TEXT NOT NULL,
    "Date" DATE NOT NULL,
    "ReviewerName" VARCHAR(255) NOT NULL,
    "Helpfulness" INTEGER NOT NULL,
    "column_11" BIGINT NOT NULL
);
ALTER TABLE
    "Main/IndividualReview" ADD PRIMARY KEY("ReviewID");
ALTER TABLE
    "Main/IndividualReview" ADD CONSTRAINT "main/individualreview_productid_foreign" FOREIGN KEY("ProductID") REFERENCES "Ratings/Reccomended"("ProductID");
ALTER TABLE
    "Characteristics" ADD CONSTRAINT "characteristics_productid_foreign" FOREIGN KEY("ProductID") REFERENCES "Ratings/Reccomended"("ProductID");
ALTER TABLE
    "Photos" ADD CONSTRAINT "photos_reviewid_foreign" FOREIGN KEY("ReviewID") REFERENCES "Main/IndividualReview"("ReviewID");