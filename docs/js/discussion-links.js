document.addEventListener('DOMContentLoaded', function() {
  // Skip if not on a content page
  if (!document.querySelector('.rst-content .document')) return;
  
  // Get the current page path (this is more reliable than the title)
  const pathname = window.location.pathname;
  const basePath = '/openscope-community-predictive-processing/';
  let pagePath = pathname.startsWith(basePath) ? pathname.substring(basePath.length) : pathname;
  // Remove trailing slash and .html extension if present
  pagePath = pagePath.replace(/\/$/, '').replace(/\.html$/, '');
  if (pagePath === '') pagePath = 'index';
  
  // Extract key identifiers from the path - this is crucial for matching discussions
  const pathParts = pagePath.split('/');
  const pageIdentifier = pathParts[pathParts.length - 1]; // Last segment of path
  
  console.log('Page path:', pagePath);
  console.log('Page identifier:', pageIdentifier);
  
  // Get the page title as a fallback
  const pageTitle = document.title.replace(' - OpenScope Community Predictive Processing', '').trim();
  console.log('Page title:', pageTitle);
  
  // Create placeholder for discussion link
  const discussionContainer = document.createElement('div');
  discussionContainer.className = 'github-discussion-link';
  discussionContainer.innerHTML = '<hr><p>Loading discussion link...</p>';
  
  // Add styling
  const style = document.createElement('style');
  style.textContent = `
    .github-discussion-link {
      margin-top: 2rem;
      padding: 1rem 0;
    }
    .github-discussion-link a {
      display: inline-block;
      padding: 0.5rem 1rem;
      border: 1px solid #ddd;
      border-radius: 4px;
      text-decoration: none;
    }
    .github-discussion-link a:hover {
      background-color: #f5f5f5;
    }
    .github-discussion-link .login-note {
      font-size: 0.8rem;
      color: #666;
      margin-top: 0.5rem;
    }
    .comment-count {
      display: inline-block;
      margin-left: 8px;
      padding: 2px 6px;
      background-color: #f1f8ff;
      border-radius: 10px;
      font-size: 0.85rem;
      color: #0366d6;
    }
  `;
  document.head.appendChild(style);
  
  // Add to page
  const content = document.querySelector('.rst-content .document');
  if (content) {
    content.appendChild(discussionContainer);
  }
  
  // Construct multiple search queries to increase chances of finding a match
  // We'll search by page path, identifier, and title
  const queries = [
    `"${pageIdentifier}" in:title repo:allenneuraldynamics/openscope-community-predictive-processing`,
    `"${pagePath}" in:title repo:allenneuraldynamics/openscope-community-predictive-processing`,
    `"Discussion: ${pageTitle}" in:title repo:allenneuraldynamics/openscope-community-predictive-processing`
  ];
  
  // Hard-coded mapping for known discussions
  const knownDiscussions = {
    'allen_institute_787727_2025-03-27': {
      id: 22,
      commentCount: 4  // Hard-coded comment count for this discussion
    }
    // Add more mappings as you create discussions
  };
  
  // Check if we have a hard-coded mapping for this page
  if (knownDiscussions[pageIdentifier]) {
    const discussionInfo = knownDiscussions[pageIdentifier];
    const discussionUrl = `https://github.com/allenneuraldynamics/openscope-community-predictive-processing/discussions/${discussionInfo.id}`;
    
    // Use the hard-coded comment count
    const commentCount = discussionInfo.commentCount || 0;
    const commentText = commentCount === 1 ? 'comment' : 'comments';
    
    discussionContainer.innerHTML = `
      <hr>
      <p>
        <a href="${discussionUrl}" target="_blank">
          💬 Join the discussion for this page on GitHub
        </a>
        <span class="comment-count">${commentCount} ${commentText}</span>
      </p>
    `;
    
    return;
  }
  
  // Otherwise try to find existing discussions through the API
  function searchWithQuery(queryIndex) {
    if (queryIndex >= queries.length) {
      // We've exhausted all queries, create a new discussion
      createNewDiscussionLink();
      return;
    }
    
    const searchQuery = encodeURIComponent(queries[queryIndex]);
    console.log('Searching with query:', queries[queryIndex]);
    
    fetch(`https://api.github.com/search/issues?q=${searchQuery}`)
      .then(response => response.json())
      .then(data => {
        console.log('GitHub API Response for query', queryIndex, ':', data);
        
        if (data.items && data.items.length > 0) {
          // Found an existing discussion or issue
          const discussion = data.items[0];
          const commentCount = discussion.comments || 0;
          const commentText = commentCount === 1 ? 'comment' : 'comments';
          
          discussionContainer.innerHTML = `
            <hr>
            <p>
              <a href="${discussion.html_url}" target="_blank">
                💬 Join the discussion for this page on GitHub
              </a>
              <span class="comment-count">${commentCount} ${commentText}</span>
            </p>
          `;
        } else {
          // Try the next query
          searchWithQuery(queryIndex + 1);
        }
      })
      .catch(error => {
        console.error('Error fetching discussions:', error);
        // Try the next query on error
        searchWithQuery(queryIndex + 1);
      });
  }
  
  function createNewDiscussionLink() {
    // No discussion exists - create new one
    discussionContainer.innerHTML = `
      <hr>
      <p>
        <a href="https://github.com/allenneuraldynamics/openscope-community-predictive-processing/discussions/new?category=q-a&title=Discussion: ${encodeURIComponent(pagePath)}" target="_blank">
          💬 Start a discussion for this page on GitHub
        </a>
        <span class="login-note">(A GitHub account is required to create or participate in discussions)</span>
      </p>
    `;
  }
  
  // Start the search process
  searchWithQuery(0);
});
