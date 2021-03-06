create table AccessCode(
  id BIGINT NOT NULL AUTO_INCREMENT,
  createdDate TIMESTAMP NOT NULL,
  modificationCounter INTEGER NOT NULL,
  code VARCHAR(4) NOT NULL,
  uuid VARCHAR(255) NOT NULL,
  startTime TIMESTAMP,
  endTime TIMESTAMP,
  status INTEGER NOT NULL,
  idQueue BIGINT NOT NULL,
  CONSTRAINT PK_AccessCode PRIMARY KEY(id),
  CONSTRAINT FK_AccessCode_idQueue FOREIGN KEY(idQueue) REFERENCES Queue(id),
);