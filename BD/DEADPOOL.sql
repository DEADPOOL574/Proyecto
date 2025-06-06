PGDMP  7                    }         
   Bd_Escuela    17.4    17.4     )           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            *           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            +           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            ,           1262    16504 
   Bd_Escuela    DATABASE     r   CREATE DATABASE "Bd_Escuela" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-ES';
    DROP DATABASE "Bd_Escuela";
                     DEADPOOL    false            �            1259    16515    recuperacion    TABLE     �   CREATE TABLE public.recuperacion (
    id integer NOT NULL,
    id_usuario integer,
    codigo character varying(10),
    usado boolean
);
     DROP TABLE public.recuperacion;
       public         heap r       DEADPOOL    false            �            1259    16514    recuperacion_id_seq    SEQUENCE     �   CREATE SEQUENCE public.recuperacion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.recuperacion_id_seq;
       public               DEADPOOL    false    220            -           0    0    recuperacion_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.recuperacion_id_seq OWNED BY public.recuperacion.id;
          public               DEADPOOL    false    219            �            1259    16506    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id integer NOT NULL,
    nombre character varying(100),
    gmail character varying(150),
    contra_hash text
);
    DROP TABLE public.usuarios;
       public         heap r       DEADPOOL    false            �            1259    16505    usuarios_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuarios_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.usuarios_id_seq;
       public               DEADPOOL    false    218            .           0    0    usuarios_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.usuarios_id_seq OWNED BY public.usuarios.id;
          public               DEADPOOL    false    217            �           2604    16518    recuperacion id    DEFAULT     r   ALTER TABLE ONLY public.recuperacion ALTER COLUMN id SET DEFAULT nextval('public.recuperacion_id_seq'::regclass);
 >   ALTER TABLE public.recuperacion ALTER COLUMN id DROP DEFAULT;
       public               DEADPOOL    false    219    220    220            �           2604    16509    usuarios id    DEFAULT     j   ALTER TABLE ONLY public.usuarios ALTER COLUMN id SET DEFAULT nextval('public.usuarios_id_seq'::regclass);
 :   ALTER TABLE public.usuarios ALTER COLUMN id DROP DEFAULT;
       public               DEADPOOL    false    217    218    218            &          0    16515    recuperacion 
   TABLE DATA           E   COPY public.recuperacion (id, id_usuario, codigo, usado) FROM stdin;
    public               DEADPOOL    false    220   Y       $          0    16506    usuarios 
   TABLE DATA           B   COPY public.usuarios (id, nombre, gmail, contra_hash) FROM stdin;
    public               DEADPOOL    false    218   v       /           0    0    recuperacion_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.recuperacion_id_seq', 1, false);
          public               DEADPOOL    false    219            0           0    0    usuarios_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.usuarios_id_seq', 1, false);
          public               DEADPOOL    false    217            �           2606    16520    recuperacion recuperacion_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.recuperacion
    ADD CONSTRAINT recuperacion_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.recuperacion DROP CONSTRAINT recuperacion_pkey;
       public                 DEADPOOL    false    220            �           2606    16513    usuarios usuarios_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT usuarios_pkey;
       public                 DEADPOOL    false    218            �           2606    16526 )   recuperacion recuperacion_id_usuario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.recuperacion
    ADD CONSTRAINT recuperacion_id_usuario_fkey FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id) NOT VALID;
 S   ALTER TABLE ONLY public.recuperacion DROP CONSTRAINT recuperacion_id_usuario_fkey;
       public               DEADPOOL    false    4750    218    220            &      x������ � �      $      x������ � �     