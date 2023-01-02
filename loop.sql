DO $$
 DECLARE
     video_id   STATISTIC.video_id%TYPE;
     viewse STATISTIC.VIEWSE%TYPE;
     comment_count STATISTIC.comment_count%TYPE;
     likes STATISTIC.likes%TYPE;
     dislikes STATISTIC.dislikes%TYPE;
 BEGIN
     video_id := 'video_number_';
     viewse := 000;
     comment_count := 000;
     likes := 000 ;
     dislikes := 000;
     FOR counter IN 10...20
         LOOP
            INSERT INTO STATISTIC (video_id,viewse,comment_count,likes,dislikes)
             VALUES (video_id || counter, viewse || counter,comment_count || counter,likes || counter,dislikes|| counter);
         END LOOP;
 END;
 $$