--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

-- Started on 2019-09-16 22:36:03

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 199 (class 1259 OID 16409)
-- Name: Aspects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Aspects" (
    "AspectId" bigint NOT NULL,
    "AspectName" text
);


ALTER TABLE public."Aspects" OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16407)
-- Name: Aspects_AspectId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Aspects_AspectId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Aspects_AspectId_seq" OWNER TO postgres;

--
-- TOC entry 2867 (class 0 OID 0)
-- Dependencies: 198
-- Name: Aspects_AspectId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Aspects_AspectId_seq" OWNED BY public."Aspects"."AspectId";


--
-- TOC entry 206 (class 1259 OID 16443)
-- Name: NormalizedSentiments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."NormalizedSentiments" (
    "NormalizedAspectId" bigint NOT NULL,
    "RawSteamReviewId" bigint NOT NULL,
    "SynonymAspectId" bigint NOT NULL,
    "Sentiment" boolean
);


ALTER TABLE public."NormalizedSentiments" OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16437)
-- Name: NormalizedSentiments_NormalizedAspectId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."NormalizedSentiments_NormalizedAspectId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."NormalizedSentiments_NormalizedAspectId_seq" OWNER TO postgres;

--
-- TOC entry 2868 (class 0 OID 0)
-- Dependencies: 203
-- Name: NormalizedSentiments_NormalizedAspectId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."NormalizedSentiments_NormalizedAspectId_seq" OWNED BY public."NormalizedSentiments"."NormalizedAspectId";


--
-- TOC entry 204 (class 1259 OID 16439)
-- Name: NormalizedSentiments_RawSteamReviewId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."NormalizedSentiments_RawSteamReviewId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."NormalizedSentiments_RawSteamReviewId_seq" OWNER TO postgres;

--
-- TOC entry 2869 (class 0 OID 0)
-- Dependencies: 204
-- Name: NormalizedSentiments_RawSteamReviewId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."NormalizedSentiments_RawSteamReviewId_seq" OWNED BY public."NormalizedSentiments"."RawSteamReviewId";


--
-- TOC entry 205 (class 1259 OID 16441)
-- Name: NormalizedSentiments_SynonymAspectId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."NormalizedSentiments_SynonymAspectId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."NormalizedSentiments_SynonymAspectId_seq" OWNER TO postgres;

--
-- TOC entry 2870 (class 0 OID 0)
-- Dependencies: 205
-- Name: NormalizedSentiments_SynonymAspectId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."NormalizedSentiments_SynonymAspectId_seq" OWNED BY public."NormalizedSentiments"."SynonymAspectId";


--
-- TOC entry 197 (class 1259 OID 16396)
-- Name: RawSteamReviews; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."RawSteamReviews" (
    "RawSteamReviewId" bigint NOT NULL,
    "RecommendedInd" text,
    "HelpfulCount" integer,
    "FunnyCount" integer,
    "HoursPlayed" integer,
    "PostedDate" text,
    "ResponseCount" integer,
    "Content" text,
    "AppId" integer DEFAULT 0,
    "NormalisedInd" boolean DEFAULT false
);


ALTER TABLE public."RawSteamReviews" OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16394)
-- Name: RawSteamReview_RawSteamReviewId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."RawSteamReview_RawSteamReviewId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."RawSteamReview_RawSteamReviewId_seq" OWNER TO postgres;

--
-- TOC entry 2871 (class 0 OID 0)
-- Dependencies: 196
-- Name: RawSteamReview_RawSteamReviewId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."RawSteamReview_RawSteamReviewId_seq" OWNED BY public."RawSteamReviews"."RawSteamReviewId";


--
-- TOC entry 202 (class 1259 OID 16422)
-- Name: SynonymAspects; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SynonymAspects" (
    "SynonymAspectId" bigint NOT NULL,
    "AspectId" bigint NOT NULL,
    "SynonymAspectName" text
);


ALTER TABLE public."SynonymAspects" OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16420)
-- Name: SynonymAspects_AspectId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SynonymAspects_AspectId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."SynonymAspects_AspectId_seq" OWNER TO postgres;

--
-- TOC entry 2872 (class 0 OID 0)
-- Dependencies: 201
-- Name: SynonymAspects_AspectId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SynonymAspects_AspectId_seq" OWNED BY public."SynonymAspects"."AspectId";


--
-- TOC entry 200 (class 1259 OID 16418)
-- Name: SynonymAspects_SynonymAspectId_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."SynonymAspects_SynonymAspectId_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."SynonymAspects_SynonymAspectId_seq" OWNER TO postgres;

--
-- TOC entry 2873 (class 0 OID 0)
-- Dependencies: 200
-- Name: SynonymAspects_SynonymAspectId_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."SynonymAspects_SynonymAspectId_seq" OWNED BY public."SynonymAspects"."SynonymAspectId";


--
-- TOC entry 2715 (class 2604 OID 16412)
-- Name: Aspects AspectId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aspects" ALTER COLUMN "AspectId" SET DEFAULT nextval('public."Aspects_AspectId_seq"'::regclass);


--
-- TOC entry 2718 (class 2604 OID 16446)
-- Name: NormalizedSentiments NormalizedAspectId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NormalizedSentiments" ALTER COLUMN "NormalizedAspectId" SET DEFAULT nextval('public."NormalizedSentiments_NormalizedAspectId_seq"'::regclass);


--
-- TOC entry 2719 (class 2604 OID 16447)
-- Name: NormalizedSentiments RawSteamReviewId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NormalizedSentiments" ALTER COLUMN "RawSteamReviewId" SET DEFAULT nextval('public."NormalizedSentiments_RawSteamReviewId_seq"'::regclass);


--
-- TOC entry 2720 (class 2604 OID 16448)
-- Name: NormalizedSentiments SynonymAspectId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NormalizedSentiments" ALTER COLUMN "SynonymAspectId" SET DEFAULT nextval('public."NormalizedSentiments_SynonymAspectId_seq"'::regclass);


--
-- TOC entry 2712 (class 2604 OID 16399)
-- Name: RawSteamReviews RawSteamReviewId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."RawSteamReviews" ALTER COLUMN "RawSteamReviewId" SET DEFAULT nextval('public."RawSteamReview_RawSteamReviewId_seq"'::regclass);


--
-- TOC entry 2716 (class 2604 OID 16425)
-- Name: SynonymAspects SynonymAspectId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SynonymAspects" ALTER COLUMN "SynonymAspectId" SET DEFAULT nextval('public."SynonymAspects_SynonymAspectId_seq"'::regclass);


--
-- TOC entry 2717 (class 2604 OID 16426)
-- Name: SynonymAspects AspectId; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SynonymAspects" ALTER COLUMN "AspectId" SET DEFAULT nextval('public."SynonymAspects_AspectId_seq"'::regclass);


--
-- TOC entry 2874 (class 0 OID 0)
-- Dependencies: 198
-- Name: Aspects_AspectId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Aspects_AspectId_seq"', 1, false);


--
-- TOC entry 2875 (class 0 OID 0)
-- Dependencies: 203
-- Name: NormalizedSentiments_NormalizedAspectId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."NormalizedSentiments_NormalizedAspectId_seq"', 1, false);


--
-- TOC entry 2876 (class 0 OID 0)
-- Dependencies: 204
-- Name: NormalizedSentiments_RawSteamReviewId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."NormalizedSentiments_RawSteamReviewId_seq"', 1, false);


--
-- TOC entry 2877 (class 0 OID 0)
-- Dependencies: 205
-- Name: NormalizedSentiments_SynonymAspectId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."NormalizedSentiments_SynonymAspectId_seq"', 1, false);


--
-- TOC entry 2878 (class 0 OID 0)
-- Dependencies: 196
-- Name: RawSteamReview_RawSteamReviewId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."RawSteamReview_RawSteamReviewId_seq"', 1, false);


--
-- TOC entry 2879 (class 0 OID 0)
-- Dependencies: 201
-- Name: SynonymAspects_AspectId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SynonymAspects_AspectId_seq"', 1, false);


--
-- TOC entry 2880 (class 0 OID 0)
-- Dependencies: 200
-- Name: SynonymAspects_SynonymAspectId_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."SynonymAspects_SynonymAspectId_seq"', 1, false);


--
-- TOC entry 2724 (class 2606 OID 16417)
-- Name: Aspects Aspects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Aspects"
    ADD CONSTRAINT "Aspects_pkey" PRIMARY KEY ("AspectId");


--
-- TOC entry 2722 (class 2606 OID 16404)
-- Name: RawSteamReviews RawSteamReview_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."RawSteamReviews"
    ADD CONSTRAINT "RawSteamReview_pkey" PRIMARY KEY ("RawSteamReviewId");


--
-- TOC entry 2726 (class 2606 OID 16428)
-- Name: SynonymAspects SynonymAspects_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SynonymAspects"
    ADD CONSTRAINT "SynonymAspects_pkey" PRIMARY KEY ("SynonymAspectId");


--
-- TOC entry 2727 (class 2606 OID 16429)
-- Name: SynonymAspects AspectId_Aspects_aspectId; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SynonymAspects"
    ADD CONSTRAINT "AspectId_Aspects_aspectId" FOREIGN KEY ("AspectId") REFERENCES public."Aspects"("AspectId");


--
-- TOC entry 2728 (class 2606 OID 16449)
-- Name: NormalizedSentiments RawSteamReviews_foreignKey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NormalizedSentiments"
    ADD CONSTRAINT "RawSteamReviews_foreignKey" FOREIGN KEY ("RawSteamReviewId") REFERENCES public."RawSteamReviews"("RawSteamReviewId");


--
-- TOC entry 2729 (class 2606 OID 16454)
-- Name: NormalizedSentiments SynonymAspects_foreignKey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."NormalizedSentiments"
    ADD CONSTRAINT "SynonymAspects_foreignKey" FOREIGN KEY ("RawSteamReviewId") REFERENCES public."RawSteamReviews"("RawSteamReviewId");


-- Completed on 2019-09-16 22:36:05

--
-- PostgreSQL database dump complete
--

