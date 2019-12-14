CREATE TABLE [DVD]
( 
	[Product_ID_ASIN]    varchar(25)  NOT NULL ,
	[DVD_title]          varchar(400)  NULL ,
	[DVD_salesrank]      int  		   NULL ,
	[DVD_avg_rating]     numeric(2,1)  NULL 
)
go

ALTER TABLE [DVD]
	ADD CONSTRAINT [XPKDVD] PRIMARY KEY  CLUSTERED ([Product_ID_ASIN] ASC)
	
	
CREATE TABLE [Product]
( 
	[Product_ID_ASIN]    varchar(25)  NOT NULL ,
	[Product_group]      varchar(18)  NULL 
)
go

ALTER TABLE [Product]
	ADD CONSTRAINT [XPKProduct] PRIMARY KEY  CLUSTERED ([Product_ID_ASIN] ASC)
	
	
	CREATE TABLE [Similar]
( 
	[Product_ID_ASIN]    varchar(25)  NOT NULL ,
	[Similar_ID_ASIN]    varchar(25)  NOT NULL ,
)
go

ALTER TABLE [Similar]
	ADD CONSTRAINT [XPKSimilar] PRIMARY KEY  CLUSTERED ([Product_ID_ASIN] ASC,[Similar_ID_ASIN] ASC)