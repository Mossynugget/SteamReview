-- Table: public."RawSteamReviews"

-- DROP TABLE public."RawSteamReviews";

CREATE TABLE public."RawSteamReviews"
(
    "RecommendedInd" text COLLATE pg_catalog."default",
    "HelpfulCount" integer,
    "FunnyCount" integer,
    "HoursPlayed" integer,
    "PostedDate" text COLLATE pg_catalog."default",
    "ResponseCount" integer,
    "Content" text COLLATE pg_catalog."default",
    "AppId" integer DEFAULT 0,
    "NormalisedInd" boolean DEFAULT false,
    "RawSteamReviewId" bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 )
)

TABLESPACE pg_default;

ALTER TABLE public."RawSteamReviews"
    OWNER to postgres;

-- Table: public."NormalizedSentiments"

-- DROP TABLE public."NormalizedSentiments";

CREATE TABLE public."NormalizedSentiments"
(
    "Keyword" text COLLATE pg_catalog."default" NOT NULL,
    "NormalizedSentimentId" bigint DEFAULT nextval('"NormalizedSentiments_NormalizedSentimentId_seq"'::regclass),
    "Weighting" numeric,
    "Positive" integer
)

TABLESPACE pg_default;

ALTER TABLE public."NormalizedSentiments"
    OWNER to postgres;