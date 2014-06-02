
/*contenttypes*/
CREATE TABLE "django_content_type" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
);
/*sessions*/
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" timestamp with time zone NOT NULL
);
CREATE INDEX "django_session_session_key_like" ON "django_session" ("session_key" varchar_pattern_ops);
CREATE INDEX "django_session_expire_date" ON "django_session" ("expire_date");
/*auth*/
CREATE TABLE "auth_user" (
    "id" serial NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" timestamp with time zone NOT NULL,
    "is_superuser" boolean NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" boolean NOT NULL,
    "is_active" boolean NOT NULL,
    "date_joined" timestamp with time zone NOT NULL
);
CREATE TABLE "auth_group" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
);
CREATE TABLE "auth_permission" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
);
CREATE TABLE "auth_group_permissions" (
    "id" serial NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("group_id", "permission_id")
);

ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "group_id_refs_id_f4b32aac" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE "auth_user_groups" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("user_id", "group_id")
);
CREATE TABLE "auth_user_user_permissions" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("user_id", "permission_id")
);

ALTER TABLE "auth_user_groups" ADD CONSTRAINT "user_id_refs_id_40c41112" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "user_id_refs_id_4dc23c39" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "auth_permission_content_type_id" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_group_id" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_name_like" ON "auth_group" ("name" varchar_pattern_ops);
CREATE INDEX "auth_user_groups_user_id" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_user_id" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "auth_user_username_like" ON "auth_user" ("username" varchar_pattern_ops);


/*admin*/
CREATE TABLE "django_admin_log" (
    "id" serial NOT NULL PRIMARY KEY,
    "action_time" timestamp with time zone NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "content_type_id" integer REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint CHECK ("action_flag" >= 0) NOT NULL,
    "change_message" text NOT NULL
);
CREATE INDEX "django_admin_log_user_id" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_content_type_id" ON "django_admin_log" ("content_type_id");

/*todo*/
CREATE TABLE "todo_proyecto" (
    "id" serial NOT NULL PRIMARY KEY,
    "nombre" varchar(45) NOT NULL,
    "descripcion" varchar(45) NOT NULL,
    "fechacreacion" date NOT NULL,
    "fechainicio" date,
    "fechafin" date,
    "estado" varchar(1)
)
;
CREATE TABLE "todo_fase" (
    "id" serial NOT NULL PRIMARY KEY,
    "fkproyecto_id" integer NOT NULL REFERENCES "todo_proyecto" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "nroorden" integer NOT NULL,
    "descripcion" varchar(45) NOT NULL,
    "fechacreacion" date NOT NULL,
    "fechainicio" date,
    "fechafin" date,
    "estado" varchar(1)
)
;
CREATE TABLE "todo_tipoitem" (
    "id" serial NOT NULL PRIMARY KEY,
    "fase_id" integer NOT NULL REFERENCES "todo_fase" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "descripcion" varchar(45) NOT NULL
)
;
CREATE TABLE "todo_atributotipoitem" (
    "id" serial NOT NULL PRIMARY KEY,
    "tipoitem_id" integer NOT NULL REFERENCES "todo_tipoitem" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "descripcion" varchar(45) NOT NULL
)
;
CREATE TABLE "todo_lineabase" (
    "id" serial NOT NULL PRIMARY KEY,
    "fase_id" integer NOT NULL REFERENCES "todo_fase" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "fechacreacion" date NOT NULL,
    "estado" varchar(1)
)
;
CREATE TABLE "todo_item" (
    "id" serial NOT NULL PRIMARY KEY,
    "tipoitem_id" integer NOT NULL REFERENCES "todo_tipoitem" ("id") DEFERRABLE INITIALLY DEFERRED,
    "lineabase_id" integer REFERENCES "todo_lineabase" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "descripcion" varchar(45) NOT NULL,
    "complejidad" integer NOT NULL,
    "costo" integer NOT NULL,
    "estado" varchar(1),
    "version" integer NOT NULL,
    "complejidadtotal" integer NOT NULL,
    "costototal" integer NOT NULL,
    "fechamodificacion" date NOT NULL
)
;
CREATE TABLE "todo_atributoitem" (
    "id" serial NOT NULL PRIMARY KEY,
    "item_id" integer NOT NULL REFERENCES "todo_item" ("id") DEFERRABLE INITIALLY DEFERRED,
    "atributotipoitem_id" integer NOT NULL REFERENCES "todo_atributotipoitem" ("id") DEFERRABLE INITIALLY DEFERRED,
    "nombre" varchar(45) NOT NULL,
    "descripcion" varchar(45) NOT NULL
)
;
CREATE TABLE "todo_relacionitem" (
    "id" serial NOT NULL PRIMARY KEY,
    "itemorigen_id" integer NOT NULL REFERENCES "todo_item" ("id") DEFERRABLE INITIALLY DEFERRED,
    "tiporelacion" varchar(1) NOT NULL,
    "itemdestino_id" integer NOT NULL REFERENCES "todo_item" ("id") DEFERRABLE INITIALLY DEFERRED
)
;
CREATE INDEX "todo_fase_fkproyecto_id" ON "todo_fase" ("fkproyecto_id");
CREATE INDEX "todo_tipoitem_fase_id" ON "todo_tipoitem" ("fase_id");
CREATE INDEX "todo_atributotipoitem_tipoitem_id" ON "todo_atributotipoitem" ("tipoitem_id");
CREATE INDEX "todo_lineabase_fase_id" ON "todo_lineabase" ("fase_id");
CREATE INDEX "todo_item_tipoitem_id" ON "todo_item" ("tipoitem_id");
CREATE INDEX "todo_item_lineabase_id" ON "todo_item" ("lineabase_id");
CREATE INDEX "todo_atributoitem_item_id" ON "todo_atributoitem" ("item_id");
CREATE INDEX "todo_atributoitem_atributotipoitem_id" ON "todo_atributoitem" ("atributotipoitem_id");
CREATE INDEX "todo_relacionitem_itemorigen_id" ON "todo_relacionitem" ("itemorigen_id");
CREATE INDEX "todo_relacionitem_itemdestino_id" ON "todo_relacionitem" ("itemdestino_id");

/*poblacion*/ 

insert into django_session (session_key,session_data,expire_date)values ('0ej8lbkm0pcohqpvg9bjryqukepenksy','OWJkOTU4MzJmMzUwM2VhODQwZmQ5NTJkMDkzZjUyYzc4Y2RhNWJhYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=wiX2F1dGhfdXNlcl9pZCI6MX0=','2014-05-26 16:22:47.785526-03');

insert into auth_user (username,password,is_superuser,is_staff,is_active,last_login,first_name,last_name,email,date_joined) values ('josea','pbkdf2_sha256$12000$xWxAuf7rt5Wd$i81nGBUNVp3+bz8zguLEVNxYNWsic029C5R54UCMi0U=','yes','yes','yes','2014-05-14','Jose','Santacruz','joseasantacruz@gmail.com','2014-05-14');
insert into auth_user (username,password,is_superuser,is_staff,is_active,last_login,first_name,last_name,email,date_joined) values ('jose','pbkdf2_sha256$12000$jwANxfhl36Ce$0i5m0y2NEc+SGB4iiSIuXO15+4e9jvU+7qrHRW6AXOM=','yes','yes','yes','2014-05-14','Jose','Pino','josepino@gmail.com','2014-05-14');
insert into auth_user (username,password,is_superuser,is_staff,is_active,last_login,first_name,last_name,email,date_joined) values ('vavi','pbkdf2_sha256$12000$9vQHgWDenQZm$wVg077k7iQSIYnvUF21yXBPE3EQTfUvbPigROKxDH4M=','yes','yes','yes','2014-05-14','Victor','Vera','victotvera@gmail.com','2014-05-14');
insert into auth_user (username,password,is_superuser,is_staff,is_active,last_login,first_name,last_name,email,date_joined) values ('juan','pbkdf2_sha256$12000$Twp4fwOYp7p4$B3iaVWwZcqOaddNyKtyWrt6R+4CkomXKv3qUjoQHq4k=','no','yes','yes','2014-05-14','Juan','Perez','juan@gmail.com','2014-05-14');
insert into auth_user (username,password,is_superuser,is_staff,is_active,last_login,first_name,last_name,email,date_joined) values ('pedro','pbkdf2_sha256$12000$tVwnJSGpK3rm$xqpAg0Fc1BXsgsFdMR+GvCuOXYSI9kwANLPu/tvem7Y=','no','yes','yes','2014-05-14','Pedro','Sanchez','pedro@gmail.com','2014-05-14');

insert into auth_group (name)values ('Administrador');
insert into auth_group (name)values ('Lider de Proyecto');
insert into auth_group (name)values ('Desarrollador');

insert into auth_user_groups (user_id,group_id)values ('1','1');
insert into auth_user_groups (user_id,group_id)values ('2','1');
insert into auth_user_groups (user_id,group_id)values ('3','1');
insert into auth_user_groups (user_id,group_id)values ('4','3');
insert into auth_user_groups (user_id,group_id)values ('5','3');


insert into django_content_type (name,app_label,model)values ('permission','auth','permission');
insert into django_content_type (name,app_label,model)values ('group','auth','group');
insert into django_content_type (name,app_label,model)values ('user','auth','user');
insert into django_content_type (name,app_label,model)values ('content type','contenttypes','contenttype');
insert into django_content_type (name,app_label,model)values ('session','sessions','session');
insert into django_content_type (name,app_label,model)values ('log entry','admin','logentry');
insert into django_content_type (name,app_label,model)values ('proyecto','todo','proyecto');
insert into django_content_type (name,app_label,model)values ('Fase','todo','fase');
insert into django_content_type (name,app_label,model)values ('TipoItem','todo','tipoitem');
insert into django_content_type (name,app_label,model)values ('Atributo del Tipo Item','todo','atributotipoitem');
insert into django_content_type (name,app_label,model)values ('Linea Base','todo','lineabase');
insert into django_content_type (name,app_label,model)values ('Item','todo','item');
insert into django_content_type (name,app_label,model)values ('Atributo del Item','todo','atributoitem');
insert into django_content_type (name,app_label,model)values ('Relacion Item','todo','relacionitem');

insert into auth_permission (name,content_type_id,codename)values ('Can add permission','1','add_permission');
insert into auth_permission (name,content_type_id,codename)values ('Can change permission','1','change_permission');
insert into auth_permission (name,content_type_id,codename)values ('Can delete permission','1','delete_permission');
insert into auth_permission (name,content_type_id,codename)values ('Can add group','2','add_group');
insert into auth_permission (name,content_type_id,codename)values ('Can change group','2','change_group');
insert into auth_permission (name,content_type_id,codename)values ('Can delete group','2','delete_group');
insert into auth_permission (name,content_type_id,codename)values ('Can add user','3','add_user');
insert into auth_permission (name,content_type_id,codename)values ('Can change user','3','change_user');
insert into auth_permission (name,content_type_id,codename)values ('Can delete user','3','delete_user');
insert into auth_permission (name,content_type_id,codename)values ('Can add contenttype','4','add_contenttype');
insert into auth_permission (name,content_type_id,codename)values ('Can change contenttype','4','change_contenttype');
insert into auth_permission (name,content_type_id,codename)values ('Can delete contenttype','4','delete_contenttype');
insert into auth_permission (name,content_type_id,codename)values ('Can add session','5','add_session');
insert into auth_permission (name,content_type_id,codename)values ('Can change session','5','change_session');
insert into auth_permission (name,content_type_id,codename)values ('Can delete session','5','delete_session');
insert into auth_permission (name,content_type_id,codename)values ('Can add log entry','6','add_logentry');
insert into auth_permission (name,content_type_id,codename)values ('Can change log entry','6','change_logentry');
insert into auth_permission (name,content_type_id,codename)values ('Can delete log entry','6','delete_logentry');
insert into auth_permission (name,content_type_id,codename)values ('Can add proyecto','7','add_proyecto');
insert into auth_permission (name,content_type_id,codename)values ('Can change proyecto','7','change_proyecto');
insert into auth_permission (name,content_type_id,codename)values ('Can delete proyecto','7','delete_proyecto');
insert into auth_permission (name,content_type_id,codename)values ('Puede visualizar el proyecto','7','ver_proyecto');
insert into auth_permission (name,content_type_id,codename)values ('Puede iniciar el proyecto','7','iniciar_proyecto');
insert into auth_permission (name,content_type_id,codename)values ('Puede administrar el proyecto que le fue designado','7','administrar_proyecto_designado');
insert into auth_permission (name,content_type_id,codename)values ('Can add fase','8','add_fase');
insert into auth_permission (name,content_type_id,codename)values ('Can change fase','8','change_fase');
insert into auth_permission (name,content_type_id,codename)values ('Can delete fase','8','delete_fase');
insert into auth_permission (name,content_type_id,codename)values ('Can add tipoitem','9','add_tipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can change tipo item','9','change_tipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can delete tipo item','9','delete_tipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can add atributo del tipo item','10','add_atributotipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can change atributo del tipo item','10','change_atributotipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can delete atributo del tipo item','10','delete_atributotipoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can add linea base','11','add_lineabase');
insert into auth_permission (name,content_type_id,codename)values ('Can change linea base','11','change_lineabase');
insert into auth_permission (name,content_type_id,codename)values ('Can delete linea base','11','delete_lineabase');
insert into auth_permission (name,content_type_id,codename)values ('Can add item','12','add_item');
insert into auth_permission (name,content_type_id,codename)values ('Can change item','12','change_item');
insert into auth_permission (name,content_type_id,codename)values ('Can delete item','12','delete_item');
insert into auth_permission (name,content_type_id,codename)values ('Can add atributo del item','13','add_atributoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can change atributo del item','13','change_atributoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can delete atributo del item','13','delete_atributoitem');
insert into auth_permission (name,content_type_id,codename)values ('Can add relacion item','14','add_relacionitem');
insert into auth_permission (name,content_type_id,codename)values ('Can change relacion item','14','change_relacionitem');
insert into auth_permission (name,content_type_id,codename)values ('Can delete relacion item','14','delete_relacionitem');


insert into auth_group_permissions (group_id,permission_id)values ('1','1');
insert into auth_group_permissions (group_id,permission_id)values ('1','2');
insert into auth_group_permissions (group_id,permission_id)values ('1','3');
insert into auth_group_permissions (group_id,permission_id)values ('1','4');
insert into auth_group_permissions (group_id,permission_id)values ('1','5');
insert into auth_group_permissions (group_id,permission_id)values ('1','6');
insert into auth_group_permissions (group_id,permission_id)values ('1','7');
insert into auth_group_permissions (group_id,permission_id)values ('1','8');
insert into auth_group_permissions (group_id,permission_id)values ('1','9');
insert into auth_group_permissions (group_id,permission_id)values ('1','10');
insert into auth_group_permissions (group_id,permission_id)values ('1','11');
insert into auth_group_permissions (group_id,permission_id)values ('1','12');
insert into auth_group_permissions (group_id,permission_id)values ('1','13');
insert into auth_group_permissions (group_id,permission_id)values ('1','14');
insert into auth_group_permissions (group_id,permission_id)values ('1','15');
insert into auth_group_permissions (group_id,permission_id)values ('1','16');
insert into auth_group_permissions (group_id,permission_id)values ('1','17');
insert into auth_group_permissions (group_id,permission_id)values ('1','18');
insert into auth_group_permissions (group_id,permission_id)values ('1','19');
insert into auth_group_permissions (group_id,permission_id)values ('1','20');
insert into auth_group_permissions (group_id,permission_id)values ('1','21');
insert into auth_group_permissions (group_id,permission_id)values ('1','22');
insert into auth_group_permissions (group_id,permission_id)values ('1','23');
insert into auth_group_permissions (group_id,permission_id)values ('1','24');
insert into auth_group_permissions (group_id,permission_id)values ('1','25');
insert into auth_group_permissions (group_id,permission_id)values ('1','26');
insert into auth_group_permissions (group_id,permission_id)values ('1','27');
insert into auth_group_permissions (group_id,permission_id)values ('1','28');
insert into auth_group_permissions (group_id,permission_id)values ('1','29');
insert into auth_group_permissions (group_id,permission_id)values ('1','30');
insert into auth_group_permissions (group_id,permission_id)values ('1','31');
insert into auth_group_permissions (group_id,permission_id)values ('1','32');
insert into auth_group_permissions (group_id,permission_id)values ('1','33');
insert into auth_group_permissions (group_id,permission_id)values ('1','34');
insert into auth_group_permissions (group_id,permission_id)values ('1','35');
insert into auth_group_permissions (group_id,permission_id)values ('1','36');
insert into auth_group_permissions (group_id,permission_id)values ('1','37');
insert into auth_group_permissions (group_id,permission_id)values ('1','38');
insert into auth_group_permissions (group_id,permission_id)values ('1','39');
insert into auth_group_permissions (group_id,permission_id)values ('1','40');
insert into auth_group_permissions (group_id,permission_id)values ('1','41');
insert into auth_group_permissions (group_id,permission_id)values ('1','42');
insert into auth_group_permissions (group_id,permission_id)values ('1','43');
insert into auth_group_permissions (group_id,permission_id)values ('1','44');
insert into auth_group_permissions (group_id,permission_id)values ('1','45');

insert into auth_group_permissions (group_id,permission_id)values ('2','20');
insert into auth_group_permissions (group_id,permission_id)values ('2','22');
insert into auth_group_permissions (group_id,permission_id)values ('2','23');
insert into auth_group_permissions (group_id,permission_id)values ('2','24');
insert into auth_group_permissions (group_id,permission_id)values ('2','25');
insert into auth_group_permissions (group_id,permission_id)values ('2','26');
insert into auth_group_permissions (group_id,permission_id)values ('2','27');
insert into auth_group_permissions (group_id,permission_id)values ('2','28');
insert into auth_group_permissions (group_id,permission_id)values ('2','29');
insert into auth_group_permissions (group_id,permission_id)values ('2','30');
insert into auth_group_permissions (group_id,permission_id)values ('2','31');
insert into auth_group_permissions (group_id,permission_id)values ('2','32');
insert into auth_group_permissions (group_id,permission_id)values ('2','33');
insert into auth_group_permissions (group_id,permission_id)values ('2','34');
insert into auth_group_permissions (group_id,permission_id)values ('2','35');
insert into auth_group_permissions (group_id,permission_id)values ('2','36');
insert into auth_group_permissions (group_id,permission_id)values ('2','37');
insert into auth_group_permissions (group_id,permission_id)values ('2','38');
insert into auth_group_permissions (group_id,permission_id)values ('2','39');
insert into auth_group_permissions (group_id,permission_id)values ('2','40');
insert into auth_group_permissions (group_id,permission_id)values ('2','41');
insert into auth_group_permissions (group_id,permission_id)values ('2','42');
insert into auth_group_permissions (group_id,permission_id)values ('2','43');
insert into auth_group_permissions (group_id,permission_id)values ('2','44');
insert into auth_group_permissions (group_id,permission_id)values ('2','45');

insert into auth_group_permissions (group_id,permission_id)values ('3','20');
insert into auth_group_permissions (group_id,permission_id)values ('3','22');
insert into auth_group_permissions (group_id,permission_id)values ('3','25');
insert into auth_group_permissions (group_id,permission_id)values ('3','26');
insert into auth_group_permissions (group_id,permission_id)values ('3','27');
insert into auth_group_permissions (group_id,permission_id)values ('3','28');
insert into auth_group_permissions (group_id,permission_id)values ('3','29');
insert into auth_group_permissions (group_id,permission_id)values ('3','30');
insert into auth_group_permissions (group_id,permission_id)values ('3','31');
insert into auth_group_permissions (group_id,permission_id)values ('3','32');
insert into auth_group_permissions (group_id,permission_id)values ('3','33');
insert into auth_group_permissions (group_id,permission_id)values ('3','34');
insert into auth_group_permissions (group_id,permission_id)values ('3','35');
insert into auth_group_permissions (group_id,permission_id)values ('3','36');
insert into auth_group_permissions (group_id,permission_id)values ('3','37');
insert into auth_group_permissions (group_id,permission_id)values ('3','38');
insert into auth_group_permissions (group_id,permission_id)values ('3','39');
insert into auth_group_permissions (group_id,permission_id)values ('3','40');
insert into auth_group_permissions (group_id,permission_id)values ('3','41');
insert into auth_group_permissions (group_id,permission_id)values ('3','42');
insert into auth_group_permissions (group_id,permission_id)values ('3','43');
insert into auth_group_permissions (group_id,permission_id)values ('3','44');
insert into auth_group_permissions (group_id,permission_id)values ('3','45');

insert into todo_proyecto ( Nombre, Descripcion, FechaCreacion, Estado)values ('Proyecto 1','Proyecto 1',current_date, 'I');
insert into todo_proyecto ( Nombre, Descripcion, FechaCreacion, Estado)values ('Proyecto 2','Proyecto 2',current_date, 'I');

insert into todo_fase (fkproyecto_id,Nombre,NroOrden,Descripcion,FechaCreacion,Estado)values ('1','Fase 1','1','Fase 1 proy1',current_date,'I');
insert into todo_fase (fkproyecto_id,Nombre,NroOrden,Descripcion,FechaCreacion,Estado)values ('1','Fase 2','2','Fase 2 proy1',current_date,'I');
insert into todo_fase (fkproyecto_id,Nombre,NroOrden,Descripcion,FechaCreacion,Estado)values ('2','Fase 1','1','Fase 1 proy2',current_date,'I');
insert into todo_fase (fkproyecto_id,Nombre,NroOrden,Descripcion,FechaCreacion,Estado)values ('2','Fase 2','2','Fase 2 proy2',current_date,'I');

insert into todo_tipoitem (fase_id,nombre,descripcion) values ('1', 'tipo a', 'tipo de item a f1p1');
insert into todo_tipoitem (fase_id,nombre,descripcion) values ('2', 'tipo b', 'tipo de item b f2p1');
insert into todo_tipoitem (fase_id,nombre,descripcion) values ('3', 'tipo c', 'tipo de item c f1p2');
insert into todo_tipoitem (fase_id,nombre,descripcion) values ('4', 'tipo d', 'tipo de item d f2p2');

insert into todo_atributotipoitem (tipoitem_id,nombre,descripcion) values ('1','atributo 1','atrib 1 tipo de item a f1p1');
insert into todo_atributotipoitem (tipoitem_id,nombre,descripcion) values ('1','atributo 2','atrib 2 tipo de item b f1p1');
insert into todo_atributotipoitem (tipoitem_id,nombre,descripcion) values ('3','atributo 1','atrib 1 tipo de item c f1p2');

insert into todo_lineabase (fase_id,nombre,fechacreacion,estado) values ('1','lb1 p1f1',current_date,'I');
insert into todo_lineabase (fase_id,nombre,fechacreacion,estado) values ('3','lb1 p2f1',current_date,'I');

insert into todo_item (tipoitem_id,nombre,descripcion,complejidad,estado,version,costo,fechamodificacion,lineabase_id,complejidadtotal,costototal) values ('1','item 1','item 1 del tipo a','5','A','1','50',current_date,'1','5','50');
insert into todo_item (tipoitem_id,nombre,descripcion,complejidad,estado,version,costo,fechamodificacion,complejidadtotal,costototal) values ('2','item 2','item 1 del tipo b','3','M','1','35',current_date,'3','35');
insert into todo_item (tipoitem_id,nombre,descripcion,complejidad,estado,version,costo,fechamodificacion,lineabase_id,complejidadtotal,costototal) values ('3','item 3','item 1 del tipo c','8','A','1','75',current_date,'2','8','75');
insert into todo_item (tipoitem_id,nombre,descripcion,complejidad,estado,version,costo,fechamodificacion,complejidadtotal,costototal) values ('4','item 4','item 1 del tipo d','2','M','1','20',current_date,'2','20');
insert into todo_item (tipoitem_id,nombre,descripcion,complejidad,estado,version,costo,fechamodificacion,lineabase_id,complejidadtotal,costototal) values ('1','item 5','item 5 del tipo a','3','A','1','45',current_date,'1','3','45');

insert into todo_atributoitem (item_id,atributotipoitem_id,nombre,descripcion) values ('1','1','atributo 1','atrib 1 del item 1');
insert into todo_atributoitem (item_id,atributotipoitem_id,nombre,descripcion) values ('1','2','atributo 2','atrib 2 del item 1');
insert into todo_atributoitem (item_id,atributotipoitem_id,nombre,descripcion) values ('3','3','atributo 1','atrib 1 del item 3');

insert into todo_relacionitem (itemorigen_id,tiporelacion,itemdestino_id) values ('1','A','2');
insert into todo_relacionitem (itemorigen_id,tiporelacion,itemdestino_id) values ('3','A','4');
insert into todo_relacionitem (itemorigen_id,tiporelacion,itemdestino_id) values ('1','P','5');







