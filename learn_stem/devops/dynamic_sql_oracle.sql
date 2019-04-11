--dynamic SQL    
set serveroutput on
DECLARE
	stmt_sql VARCHAR2(1000);
	v_hier VARCHAR2(50);
	v_country VARCHAR2(2) := 'US';
	v_schema VARCHAR2(50) := 'WGONG';
	v_sys_name VARCHAR2(10) := 'GEC';
BEGIN
	stmt_sql:= 'select geo_hier from ' ||v_schema|| '.OALCDM_GEO_HIER_CFG where country=''' ||v_country|| ''' and system_name= ''' ||v_sys_name||'''' ;
    Dbms_output.put_line(' stmt_sql: '||stmt_sql);
    
	EXECUTE IMMEDIATE stmt_sql INTO v_hier;
	Dbms_output.put_line(' geo_hier: '||v_hier);
END;
/


upd_sql_child := 'UPDATE '||TABLE_NAME||' SET '||STATUS_FLAG_NAME||' = '||status_enddate_new||
        ', last_update_date = systimestamp, last_updated_by = ''oal-data-migration_us@oracle.com'' '||
        'where '||table_name_key||' = '||react_item.owner_table_key1||' and '||status_flag_name||st_ed_react||status_enddate;
                                                    
execute immediate upd_sql_child;


--https://livesql.oracle.com/apex/livesql/file/content_CIREYU9EA54EOKQ7LAMZKRF6P.html
--paired quotes
set serveroutput on
BEGIN  
   --DBMS_OUTPUT.put_line ('That''s a really funny ''joke''.');  
   DBMS_OUTPUT.PUT_LINE (  
       q'!What's a quote among friends?!'
   );
END; 

SELECT q'#All the President's men#'  FROM  DUAL;
SELECT q'[All the President's men]'  FROM  DUAL;
select to_char(100) from dual;

--binding var
declare
v_input1 VARCHAR2(20) := 'Whoa!';
v_input2 NUMBER := 123;
v_SQL_STR VARCHAR2(1000) := null;
begin

    v_SQL_STR := q'[
        declare
        v_output VARCHAR2(100) := NULL;
        begin
            dbms_output.put_line('- ' || :1 || '-');
            select 'Output: ' || :2 || ' => ' || to_char(:3) into v_output from dual;
            dbms_output.put_line(v_output);
        end;
    ]';
    
    DBMS_OUTPUT.PUT_LINE('Dynamic SQL: ');
    DBMS_OUTPUT.PUT_LINE('=========================');
    DBMS_OUTPUT.PUT_LINE(v_SQL_STR);
    DBMS_OUTPUT.PUT_LINE('=========================');
    
    execute immediate v_SQL_STR using v_input1, v_input1, v_input2;

end;
/
