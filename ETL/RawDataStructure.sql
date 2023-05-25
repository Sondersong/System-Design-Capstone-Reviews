CREATE TABLE "Characteristics"(
    "id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Characteristics" ADD PRIMARY KEY("id");
CREATE TABLE "Reviews_Photos"(
    "id" BIGINT NOT NULL,
    "review_id" BIGINT NOT NULL,
    "url" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Reviews_Photos" ADD PRIMARY KEY("id");
CREATE TABLE "Reviews"(
    "id" BIGINT NOT NULL,
    "product_id" BIGINT NOT NULL,
    "rating" BIGINT NOT NULL,
    "date" BIGINT NOT NULL,
    "summary" VARCHAR(255) NOT NULL,
    "body" VARCHAR(255) NOT NULL,
    "recommend" BOOLEAN NOT NULL,
    "reported" BOOLEAN NOT NULL,
    "reviewer_name" VARCHAR(255) NOT NULL,
    "reviewer_email" VARCHAR(255) NOT NULL,
    "response" VARCHAR(255) NOT NULL,
    "helpfulness" BIGINT NOT NULL
);
ALTER TABLE
    "Reviews" ADD PRIMARY KEY("id");
CREATE TABLE "Characteristic_Reviews"(
    "id" BIGINT NOT NULL,
    "characteristic_id" BIGINT NOT NULL,
    "review_id" BIGINT NOT NULL,
    "value" BIGINT NOT NULL
);
ALTER TABLE
    "Characteristic_Reviews" ADD PRIMARY KEY("id");